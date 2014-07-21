#!/bin/sh

echo 'Disabling software update (setting schedule to off)'
/usr/sbin/softwareupdate --schedule off

OS_MAJ=`uname -r | cut -d . -f 1`
# 10 = 10.6, 11 = 10.7, 12 = 10.8, 13 = 10.9

if [ $OS_MAJ -ge 10 -a $OS_MAJ -le 12 ]; then
	# 10.6-10.8

	echo 'Unloading XProtect Updater launch daemon (10.6-10.8)'

	/bin/launchctl unload -w "/System/Library/LaunchDaemons/com.apple.xprotectupdater.plist" > /dev/null 2>&1
fi

if [ $OS_MAJ -ge 12 ]; then
	# 10.8+

	echo 'Turning background updates OFF (10.8+)'
	# Note this may not be necessary if the entire SW update schedule is off. But we'll be paranoid about it.

	# for (at least) 10.8+ also disable the 'install behind my back' options
	defaults write /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall -bool false
	defaults write /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall -bool false
fi
