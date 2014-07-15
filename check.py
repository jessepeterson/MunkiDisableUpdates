import sys

if 'FlashPlayerConfig' not in locals().keys():
	# import if not running in concatenated script
	from flashconfig import FlashPlayerConfig
	from xprotmeta import AppleXProtectMeta

fpc = FlashPlayerConfig()
xpm = AppleXProtectMeta()

if not fpc.auto_updates_disabled():
	print 'Flash updates are not disabled; returning 0 (not installed)'
	sys.exit(0)

if xpm.flash_plugin_blacklisted():
	print 'Flash plugin is blacklisted; returning 0 (not installed)'
	sys.exit(0)

print 'Flash not blocked and updates disabled; returning 1 (installed)'
sys.exit(1)

