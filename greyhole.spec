Name:           greyhole
Version:        $VERSION
Release:        $BUILD_NUMBER
Summary:        Greyhole is a drive pooling technology for Samba
Group:          System Environment/Daemons
Source:         http://greyhole.googlecode.com/files/%{name}-%{version}.tar.gz
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       samba >= 3.4.3, php-cli >= 5.5, php-pdo, php-mbstring, php-intl, rsync, sysstat, lsof

%description
Greyhole allows you to create a storage pool, accessible from 
Samba shares, that offers data redundancy and JBOD concatenation.

%define debug_package %{nil}

%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/web-app/
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/web-app/du/
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/web-app/install/
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/web-app/views/
mkdir -p $RPM_BUILD_ROOT/usr/share/greyhole/scripts-examples/
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1/
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man5/

install -m 0755 -D -p greyhole ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 -D -p greyhole-dfree ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 -D -p greyhole-php ${RPM_BUILD_ROOT}%{_bindir}
install -m 0755 -D -p greyhole-dfree.php ${RPM_BUILD_ROOT}/usr/share/greyhole/
install -m 0755 -D -p build_vfs.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/

install -m 0644 -D -p schema-mysql.sql ${RPM_BUILD_ROOT}/usr/share/greyhole/
install -m 0644 -D -p greyhole.example.conf ${RPM_BUILD_ROOT}/usr/share/greyhole/

install -m 0644 -D -p greyhole.example.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/greyhole.conf
install -m 0755 -D -p initd_script.sh ${RPM_BUILD_ROOT}/etc/rc.d/init.d/greyhole
install -m 0644 -D -p logrotate.greyhole ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/greyhole
install -m 0644 -D -p greyhole.cron.d ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d/greyhole
install -m 0755 -D -p greyhole.cron.weekly ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.weekly/greyhole
install -m 0755 -D -p greyhole.cron.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/greyhole

install -m 0644 -D -p web-app/index.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/README ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/LICENSE.md ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/favicon.png ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/includes.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/init.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/config_definitions.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/scripts.js ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/styles.css ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/
install -m 0644 -D -p web-app/du/index.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/du/
install -m 0644 -D -p web-app/install/index.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step1.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step2.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step3.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step4.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step5.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step6.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/install/step7.inc.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/install/
install -m 0644 -D -p web-app/views/actions.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/
install -m 0644 -D -p web-app/views/greyhole_config.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/
install -m 0644 -D -p web-app/views/samba_config.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/
install -m 0644 -D -p web-app/views/samba_shares.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/
install -m 0644 -D -p web-app/views/status.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/
install -m 0644 -D -p web-app/views/storage_pool.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/
install -m 0644 -D -p web-app/views/trash.php ${RPM_BUILD_ROOT}/usr/share/greyhole/web-app/views/

install -m 0755 -D -p scripts-examples/greyhole_file_changed.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_idle.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_notify_error.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_send_fsck_report.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/
install -m 0755 -D -p scripts-examples/greyhole_sysadmin_notification.sh ${RPM_BUILD_ROOT}/usr/share/greyhole/scripts-examples/

install -m 0644 -D -p USAGE ${RPM_BUILD_ROOT}/usr/share/greyhole/

install -m 0644 -D -p docs/greyhole.1.gz ${RPM_BUILD_ROOT}/usr/share/man/man1/
install -m 0644 -D -p docs/greyhole-dfree.1.gz ${RPM_BUILD_ROOT}/usr/share/man/man1/
install -m 0644 -D -p docs/greyhole.conf.5.gz ${RPM_BUILD_ROOT}/usr/share/man/man5/

SUPPORTED_SAMBA_VERSIONS=`ls -1 samba-module/bin/`
%ifarch x86_64
	for v in ${SUPPORTED_SAMBA_VERSIONS}; do
		dotlessv=`echo $v | tr -d '.'`
		if [ -f samba-module/bin/${v}/greyhole-x86_64.so ]; then
			install -m 0644 -D -p samba-module/bin/${v}/greyhole-x86_64.so ${RPM_BUILD_ROOT}/usr/lib64/greyhole/greyhole-samba${dotlessv}.so
		fi
	done
%else
	%ifarch %{arm}
		for v in ${SUPPORTED_SAMBA_VERSIONS}; do
			dotlessv=`echo $v | tr -d '.'`
			if [ -f samba-module/bin/${v}/greyhole-armv5tel.so ]; then
				install -m 0644 -D -p samba-module/bin/${v}/greyhole-armv5tel.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba${dotlessv}.so
			fi
		done
	%else
		for v in ${SUPPORTED_SAMBA_VERSIONS}; do
			dotlessv=`echo $v | tr -d '.'`
			if [ -f samba-module/bin/${v}/greyhole-i386.so ]; then
				install -m 0644 -D -p samba-module/bin/${v}/greyhole-i386.so ${RPM_BUILD_ROOT}/usr/lib/greyhole/greyhole-samba${dotlessv}.so
			fi
		done
	%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
echo "Executing post-install script..."
mkdir -p /var/spool/greyhole
chmod 777 /var/spool/greyhole
/usr/bin/greyhole --create-mem-spool >/dev/null
mkdir -p /var/cache/greyhole-dfree
chmod 777 /var/cache/greyhole-dfree

if [ ! -f /usr/bin/cpgh ]; then
	ln -s /usr/bin/greyhole /usr/bin/cpgh
fi

if [ -d /usr/lib/x86_64-linux-gnu ]; then 
    SOURCE_LIBDIR="/usr/lib64"
    TARGET_LIBDIR="/usr/lib/x86_64-linux-gnu"
elif [ "`uname -m`" = "x86_64" ]; then
    SOURCE_LIBDIR="/usr/lib64"
    TARGET_LIBDIR="/usr/lib64"
else
    SOURCE_LIBDIR="/usr/lib"
    TARGET_LIBDIR="/usr/lib"
fi

TARGET_SYMLINK="${TARGET_LIBDIR}/samba/vfs/greyhole.so"

SMB_VERSION="`smbd --version | awk '{print $2}' | awk -F'-' '{print $1}' | awk -F'.' '{print $1$2}'`"
SOURCE_LIB="${SOURCE_LIBDIR}/greyhole/greyhole-samba${SMB_VERSION}.so"
if [ ! -f ${SOURCE_LIB} ]; then
	echo "Error: Greyhole doesn't include a VFS module for your version of Samba (${SMB_VERSION})."
	echo "See INSTALL file for details on how to compile it yourself, or create an issue at https://github.com/gboudreau/Greyhole/issues"
	exit 1
fi

set +e
ls -l "${TARGET_SYMLINK}" 2>/dev/null | grep '/usr/share/greyhole/vfs-build/' >/dev/null
if [ $? -eq 0 ]; then
	echo "Detected custom (locally-compiled) Greyhole VFS module at ${TARGET_SYMLINK}; will NOT overwrite it."
else
	rm -f ${TARGET_SYMLINK}
	ln -s ${SOURCE_LIB} ${TARGET_SYMLINK}
fi
set -e

if [ -f /proc/fs/cifs/OplockEnabled ]; then
	# cifs client workaround
	# Ref: http://blog.dhampir.no/content/cifs-vfs-no-response-for-cmd-n-mid
	modprobe cifs
	echo 0 > /proc/fs/cifs/OplockEnabled
fi
if [ -f /sys/module/cifs/parameters/enable_oplocks ]; then
	# cifs client workaround
	# Ref: http://blog.dhampir.no/content/cifs-vfs-no-response-for-cmd-n-mid
	modprobe cifs enable_oplocks=0
	echo 0 > /sys/module/cifs/parameters/enable_oplocks
fi

running=0
# (SYSV) Service install & start
if [ -f /sbin/chkconfig ]; then
	/sbin/chkconfig --add greyhole
	/sbin/chkconfig greyhole on
else
	/usr/sbin/update-rc.d greyhole defaults
fi
if [ -f /etc/rc.d/init.d/greyhole ]; then
	if [ "`service greyhole stat 2> /dev/null | grep 'is running' | wc -l`" = "1" ]; then
		service greyhole restart
		running=1
	fi
fi

if [ $running -eq 0 ]; then
	echo "==========================================================================="
	echo "See /usr/share/greyhole/USAGE to learn how to configure and start Greyhole."
	echo "==========================================================================="
fi

if which man >/dev/null 2>&1; then
    man logrotate >/dev/null 2>&1 || echo "Warning! logrotate is not installed. You should install logrotate to make sure the Greyhole logs don't fill your root partition.
  Greyhole already installed the necessary conf file for logrotate; simply installing the logrotate package is enough."
fi

%preun

# Delete cache folder
rm -rf /var/cache/greyhole-dfree

if [ "$1" != 0 ]; then
	set +e
	/sbin/service greyhole condrestart 2>&1 > /dev/null
	set -e
else
	# not an update, a complete uninstall

	# Delete VFS module symlinks, if any
	rm -f /usr/lib/x86_64-linux-gnu/samba/vfs/greyhole.so
	rm -f /usr/lib64/samba/vfs/greyhole.so
	rm -f /usr/lib/samba/vfs/greyhole.so

	# Service removal
	/sbin/service greyhole stop 2>&1 > /dev/null
	/sbin/chkconfig --del greyhole

	# Remove Greyhole from /etc/samba/smb.conf
	grep -v "dfree.*greyhole" /etc/samba/smb.conf > /etc/samba/smb.conf.new
	sed --in-place -e 's@\(vfs objects.*\) greyhole@\1@' /etc/samba/smb.conf.new
	sed --in-place -e 's@^[ \t]*vfs objects =$@@' /etc/samba/smb.conf.new
	mv -f /etc/samba/smb.conf.new /etc/samba/smb.conf
	/sbin/service smb reload 2>&1 > /dev/null
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/greyhole.conf
/etc/rc.d/init.d/greyhole
/etc/*/greyhole*
/usr/bin/greyhole*
%{_libdir}/greyhole/
/usr/share/greyhole/
/usr/share/man/*/greyhole*

%changelog
* Sun Jan 13 2013 Guillaume Boudreau
- Including gh-du web UI
* Sun Jan 02 2011 Guillaume Boudreau
- Fedora 14 (Samba 3.5) compatibility fixes
* Mon Mar 29 2010 Carlos Puchol
- add sqlite schema file, rename mysql one
- use /usr/share/greyhole instead of local 
* Mon Feb 22 2010 Guillaume Boudreau
- major update in all sections; more automated installation
* Wed Jan 22 2010 Carlos Puchol
- initial version of Greyhole spec
