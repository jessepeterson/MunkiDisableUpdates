import sys

if 'AppleXProtectMeta' not in locals().keys():
	# import if not running in concatenated script
	from xprotmeta import AppleXProtectMeta

xpm = AppleXProtectMeta()

print 'Removing Flash player blacklist'
xpm.remove_java_plugins_blacklist()

sys.exit(0)
