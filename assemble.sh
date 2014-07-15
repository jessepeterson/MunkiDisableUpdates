echo 'Assembling installcheck_script.py...'

echo '#!/usr/bin/python' >> installcheck_script.py
echo >> installcheck_script.py
cat xprotmeta.py >> installcheck_script.py
cat flashconfig.py >> installcheck_script.py
cat check.py  >> installcheck_script.py
chmod 755 installcheck_script.py
