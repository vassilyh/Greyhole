<?php
/*
Copyright 2009-2020 Guillaume Boudreau

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

require_once('includes/AbstractRunner.php');

abstract class AbstractCliRunner extends AbstractRunner {
    
    protected $options;
    /** @var CliCommandDefinition */
    protected $cli_command;

    function __construct($options, $cli_command) {
        parent::__construct();
        $this->options = $options;
        $this->cli_command = $cli_command;
    }

    protected function log($what='') {
        echo "$what\n";
    }
    
    protected function logn($what) {
        echo "$what";
    }

    protected function restart_service() {
        if (!DaemonRunner::restart_service()) {
            $this->log("You should now restart the Greyhole daemon.");
        }
    }

    protected function parseCmdParamAsDriveAndExpect($expectedParamValues) {
        if (isset($this->options['cmd_param'])) {
            $dir = $this->options['cmd_param'];
            if (!array_contains($expectedParamValues, $dir)) {
                $dir = '/' . trim($dir, '/');
            }
        }
        if (empty($dir) || !array_contains($expectedParamValues, $dir)) {
            return FALSE;
        }
        return $dir;
    }
}

?>
