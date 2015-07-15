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

VERS=0.2
NAME=JavaUpdatesDisable

OUTFILE=installcheck_script-java.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
echo >> $OUTFILE
cat javadeployment.py  >> $OUTFILE
echo >> $OUTFILE
cat javaupdaterpref.py  >> $OUTFILE
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
cat javadeployment.py  >> $OUTFILE
echo >> $OUTFILE
cat javaupdaterpref.py  >> $OUTFILE
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
	--installcheck_script=installcheck_script-java.py \
	--postinstall_script=postinstall_script-java.py \
	--unattended_install \
	> $NAME-$VERS.$BUILDNO.pkginfo

##################################################

echo 'Adobe Reader Updates Disable'

VERS=0.2
NAME=AdobeReaderUpdateDisable

OUTFILE=installcheck_script-reader.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat readerpref.py  >> $OUTFILE
echo >> $OUTFILE
cat reader-check.py  >> $OUTFILE
echo >> $OUTFILE
chmod 755 $OUTFILE

OUTFILE=postinstall_script-reader.py
echo "==> Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat readerpref.py  >> $OUTFILE
echo >> $OUTFILE
cat reader-disable.py  >> $OUTFILE
echo >> $OUTFILE
chmod 755 $OUTFILE

echo "==> Creating $NAME-$VERS.$BUILDNO.pkginfo"
# perhaps someday make this automatically update for Reader?
#	--update_for=AdobeReader \
/usr/local/munki/makepkginfo \
	--name=$NAME \
	--displayname='Adobe Reader Update Disable' \
	--description='Disables automatic update checking and updating for Adobe Reader.' \
	--pkgvers=$VERS.$BUILDNO \
	-c development -c testing \
	--minimum_os_version=10.6.0 \
	--nopkg \
	--installcheck_script=installcheck_script-reader.py \
	--postinstall_script=postinstall_script-reader.py \
	--unattended_install \
	> $NAME-$VERS.$BUILDNO.pkginfo

##################################################

NAME=OSXUpdatesDisable
VERS=0.6

echo 'OS X Updates Disable'
echo "==> Creating $NAME-$VERS.$BUILDNO.pkginfo"

/usr/local/munki/makepkginfo \
	--name=$NAME \
	--displayname='OS X Automatic Update Disable' \
	--description='Disables update checking for OS X.' \
	--pkgvers=$VERS.$BUILDNO \
	-c development -c testing \
	--minimum_os_version=10.6.0 \
	--nopkg \
	--installcheck_script=osx-check.sh \
	--postinstall_script=osx-disable.sh \
	--unattended_install \
	> $NAME-$VERS.$BUILDNO.pkginfo
