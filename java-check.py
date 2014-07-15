import sys

if 'AppleXProtectMeta' not in locals().keys():
	# import if not running in concatenated script
	from xprotmeta import AppleXProtectMeta

xpm = AppleXProtectMeta()

if xpm.java_plugins_blacklisted():
	print 'Java plugins are blacklisted; returning 0 (not installed)'
	sys.exit(0)

print 'Java not blacklisted; returning 1 (installed)'
sys.exit(1)
