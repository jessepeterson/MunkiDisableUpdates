#!/bin/sh

if [ ! -f .buildno ];
then
	echo 0 >> .buildno
fi
BUILDNO=`cat .buildno`
BUILDNO=`expr $BUILDNO + 1`
echo $BUILDNO > .buildno

##################################################

echo 'Flash Player Updates Disable'

VERS=0.4
NAME=AdobeFlashPlayerUpdateDisable

OUTFILE=installcheck_script-flash.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
echo >> $OUTFILE
cat flashconfig.py >> $OUTFILE
echo >> $OUTFILE
cat flash-check.py  >> $OUTFILE
echo >> $OUTFILE
chmod 755 $OUTFILE

OUTFILE=postinstall_script-flash.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
echo >> $OUTFILE
cat flashconfig.py >> $OUTFILE
echo >> $OUTFILE
cat flash-disable.py  >> $OUTFILE
echo >> $OUTFILE
chmod 755 $OUTFILE

echo "==> Creating $NAME-$VERS.$BUILDNO.pkginfo"
# perhaps someday make this automatically update for AdobeFlashPlayer?
#	--update_for=AdobeFlashPlayer \
/usr/local/munki/makepkginfo \
	--name=$NAME \
	--displayname='Adobe Flash Player Update Disable' \
	--description='Disables automatic update checking and updating for Adobe Flash.' \
	--pkgvers=$VERS.$BUILDNO \
	-c development -c testing \
	--minimum_os_version=10.6.0 \
	--nopkg \
	--installcheck_script=installcheck_script-flash.py \
	--postinstall_script=postinstall_script-flash.py \
	--unattended_install \
	> $NAME-$VERS.$BUILDNO.pkginfo

##################################################

echo 'Java Updates Disable'

VERS=0.1
NAME=JavaUpdatesDisable

OUTFILE=installcheck_script-java.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
echo >> $OUTFILE
cat java-check.py  >> $OUTFILE
echo >> $OUTFILE
chmod 755 $OUTFILE

OUTFILE=postinstall_script-java.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
echo >> $OUTFILE
cat java-disable.py  >> $OUTFILE
echo >> $OUTFILE
chmod 755 $OUTFILE

echo "==> Creating $NAME-$VERS.$BUILDNO.pkginfo"
# perhaps someday make this automatically update for Java?
#	--update_for=OracleJava7 \
/usr/local/munki/makepkginfo \
	--name=$NAME \
	--displayname='Java Update Disable' \
	--description='Disables checking of updates and expirations of Java 7.' \
	--pkgvers=$VERS.$BUILDNO \
	-c development -c testing \
	--minimum_os_version=10.7.0 \
	--nopkg \
	--installcheck_script=installcheck_script-flash.py \
	--postinstall_script=postinstall_script-flash.py \
	--unattended_install \
	> $NAME-$VERS.$BUILDNO.pkginfo
