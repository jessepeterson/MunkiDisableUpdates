import sys

if 'AdobeReaderPref' not in locals().keys():
	# import if not running in concatenated script
	from readerpref import AdobeReaderPref

rp = AdobeReaderPref()

if not rp.updates_disabled():
	print 'Adobe Reader Updates not disabled; returning 0 (not installed)'
	sys.exit(0)

print 'Adobe Reader Updates are disabled; returning 1 (installed)'
sys.exit(1)
