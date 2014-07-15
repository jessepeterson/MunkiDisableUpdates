import plistlib
import os

XPROTECT_META_FILE = '/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist'

class AppleXProtectMeta:
	def exists(self):
		return os.path.exists(XPROTECT_META_FILE)

	def read_xprotmeta(self):
		if not self.exists():
			return None

		return plistlib.readPlist(XPROTECT_META_FILE)

	def write_xprotmeta(self, xprotmeta):
		plistlib.writePlist(xprotmeta, XPROTECT_META_FILE)

	def plugin_blacklist_item_exists(self, blitem):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			return False

		if 'PlugInBlacklist' in xprotmeta.keys() and '10' in xprotmeta['PlugInBlacklist'].keys() and blitem in xprotmeta['PlugInBlacklist']['10'].keys():
			return True

		return False

	def remove_plugin_blacklist_item(self, blitem):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			return

		if 'PlugInBlacklist' in xprotmeta.keys() and '10' in xprotmeta['PlugInBlacklist'].keys() and blitem in xprotmeta['PlugInBlacklist']['10'].keys():
			del xprotmeta['PlugInBlacklist']['10'][blitem]
			self.write_xprotmeta(xprotmeta)

	def flash_plugin_blacklisted(self):
		return self.plugin_blacklist_item_exists('com.macromedia.Flash Player.plugin')

	def remove_flash_plugin_blacklist(self):
		self.remove_plugin_blacklist_item('com.macromedia.Flash Player.plugin')
