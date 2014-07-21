#!/bin/sh

SWUPD_CHECK=`/usr/sbin/softwareupdate --schedule`

if [ "X$SWUPD_CHECK" != "XAutomatic check is off" ]
then
	echo 'softwareupdate schedule is ON; returning 0 (not installed)'
	exit 0
fi

OS_MAJ=`uname -r | cut -d . -f 1`
# 10 = 10.6, 11 = 10.7, 12 = 10.8, 13 = 10.9

if [ $OS_MAJ -ge 10 -a $OS_MAJ -le 12 ]; then
	# 10.6-10.8

	/bin/launchctl list com.apple.xprotectupdater > /dev/null 2>&1
	if [ $? -eq 0 ]; then
		echo 'Launchd XProtect is loaded; returning 0 (not installed)'
		exit 0
	fi
# TODO: possibly check the ConfigDataInstall and CriticalUpdateInstall entries?
#elif [ $OS_MAJ -ge 12 ]; then
	# 10.8+
	# defaults read /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall
	# defaults read /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall
fi
