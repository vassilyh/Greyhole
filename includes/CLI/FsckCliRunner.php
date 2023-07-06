<?php
/*
Copyright 2009-2019 Guillaume Boudreau

This file is part of Greyhole.

Greyhole is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Greyhole is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Greyhole.  If not, see <http://www.gnu.org/licenses/>.
*/

require_once('includes/CLI/AbstractCliRunner.php');

define('OPTION_EMAIL', 'email');
define('OPTION_IF_CONF_CHANGED', 'if-conf-changed');
define('OPTION_CHECKSUMS','checksums');
define('OPTION_SKIP_METASTORE','skip-metastore');
define('OPTION_ORPHANED','orphaned');
define('OPTION_DU','du');
define('OPTION_DEL_ORPHANED_METADATA','del-orphaned-metadata');
define('OPTION_VALIDATE_COPIES','validate-copies-created');

class FsckCliRunner extends AbstractCliRunner {
    private $dir = '';
    private $fsck_options = array();
    
    private static $available_options = array(
       'email-report' => OPTION_EMAIL,
       'dont-walk-metadata-store' => OPTION_SKIP_METASTORE,
       'if-conf-changed' => OPTION_IF_CONF_CHANGED,
       'disk-usage-report' => OPTION_DU,
       'find-orphaned-files' => OPTION_ORPHANED,
       'checksums' => OPTION_CHECKSUMS,
       'delete-orphaned-metadata' => OPTION_DEL_ORPHANED_METADATA
    );

    function __construct($options, $cli_command) {
        parent::__construct($options, $cli_command);

        if (isset($this->options['dir'])) {
            $this->dir = $this->options['dir'];
            if (!is_dir($this->dir)) {
                $this->log("$this->dir is not a directory. Exiting.");
                $this->finish(1);
            }
        }
        
        foreach (self::$available_options as $cli_option => $option) {
            if (isset($this->options[$cli_option])) {
                $this->fsck_options[] = $option;
            }
        }
    }

    public function run() {
        if (empty($this->dir)) {
            $task_ids = schedule_fsck_all_shares($this->fsck_options);
            $this->dir = 'all shares';
            $fsck_options = NULL;
        } else {
            $query = "INSERT INTO tasks SET action = 'fsck', share = :full_path, additional_info = :fsck_options, complete = 'yes'";
            if (empty($this->fsck_options)) {
                $fsck_options = NULL;
            } else {
                $fsck_options = implode('|', $this->fsck_options);
            }
            $params = array(
                'full_path' => $this->dir,
                'fsck_options' => $fsck_options,
            );
            $task_id = DB::insert($query, $params);
            $task_ids = array($task_id);
        }

        FSCKWorkLog::initiate($this->dir, $fsck_options, $task_ids);

        $this->log("fsck of $this->dir has been scheduled. It will start after all currently pending tasks have been completed.");
        if (isset($this->options['checksums'])) {
            $this->log("Any mismatch in checksums will be logged in both " . Config::get(CONFIG_GREYHOLE_LOG_FILE) . " and " . FSCKLogFile::PATH . "/fsck_checksums.log");
        }

        // Also clean the tasks_completed table
        DB::deleteExecutedTasks();
    }

    protected function log($what='') {
        if (isset($_POST)) {
            error_log($what);
        } else {
            echo "$what\n";
        }
    }

    protected function logn($what) {
        if (isset($_POST)) {
            error_log($what);
        } else {
            echo $what;
        }
    }
}

?>
