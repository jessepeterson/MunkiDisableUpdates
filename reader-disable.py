import sys

if 'AdobeReaderPref' not in locals().keys():
	# import if not running in concatenated script
	from readerpref import AdobeReaderPref

rp = AdobeReaderPref()

print 'Disabling Adobe Reader Updates'
rp.disable_updates()

sys.exit(0)
