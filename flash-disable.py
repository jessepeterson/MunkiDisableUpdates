import sys

if 'FlashPlayerConfig' not in locals().keys():
	# import if not running in concatenated script
	from flashconfig import FlashPlayerConfig
	from xprotmeta import AppleXProtectMeta

fpc = FlashPlayerConfig()
xpm = AppleXProtectMeta()

print 'Disabling Flash player updates'
fpc.disable_auto_updates()

print 'Removing Flash player blacklist'
xpm.remove_flash_plugin_blacklist()

sys.exit(0)
