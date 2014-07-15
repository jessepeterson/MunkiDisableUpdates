#!/bin/sh

OUTFILE=installcheck_script.py
echo "Assembling $OUTFILE..."
echo '#!/usr/bin/python' >> $OUTFILE
echo >> $OUTFILE
cat xprotmeta.py >> $OUTFILE
cat flashconfig.py >> $OUTFILE
cat check.py  >> $OUTFILE
chmod 755 $OUTFILE
