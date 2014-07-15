#!/bin/sh

VERS=0.2
NAME=AdobeFlashPlayerUpdateDisable

OUTFILE=installcheck_script.py
echo "Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
cat flashconfig.py >> $OUTFILE
cat check.py  >> $OUTFILE
chmod 755 $OUTFILE

OUTFILE=postinstall_script.py
echo "Assembling $OUTFILE..."
echo '#!/usr/bin/python' > $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
cat flashconfig.py >> $OUTFILE
cat disable.py  >> $OUTFILE
chmod 755 $OUTFILE

if [ ! -f .buildno ];
then
	echo 0 >> .buildno
fi
buildno=`cat .buildno`
buildno=`expr $buildno + 1`
echo $buildno > .buildno

VERS=$VERS.$buildno

echo "Creating $NAME-$VERS.pkginfo"
# perhaps someday make this automatically update for AdobeFlashPlayer?
#	--update_for=AdobeFlashPlayer \
/usr/local/munki/makepkginfo \
	--name=$NAME \
	--displayname='Adobe Flash Player Update Disable' \
	--description='Disables automatic update checking and updating for Adobe Flash.' \
	--pkgvers=$VERS \
	-c development -c testing \
	--minimum_os_version=10.5.0 \
	--nopkg \
	--installcheck_script=installcheck_script.py \
	--postinstall_script=postinstall_script.py \
	--unattended_install \
	> $NAME-$VERS.pkginfo
