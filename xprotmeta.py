import plistlib
import os

XPROTECT_META_FILE = '/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/XProtect.meta.plist'
# XPROTECT_META_FILE = '/tmp/XProtect.meta.plist'

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

	def plugin_blacklist_items_exist(self, blitems):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			return False

		if 'PlugInBlacklist' in xprotmeta.keys() and '10' in xprotmeta['PlugInBlacklist'].keys():
			for blitem in blitems:
				if blitem in xprotmeta['PlugInBlacklist']['10'].keys():
					return True

		return False


	def remove_plugin_blacklist_item(self, blitem):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			return

		if 'PlugInBlacklist' in xprotmeta.keys() and '10' in xprotmeta['PlugInBlacklist'].keys() and blitem in xprotmeta['PlugInBlacklist']['10'].keys():
			del xprotmeta['PlugInBlacklist']['10'][blitem]
			self.write_xprotmeta(xprotmeta)

	def remove_plugin_blacklist_items(self, blitems):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			return

		modified = 0

		if 'PlugInBlacklist' in xprotmeta.keys() and '10' in xprotmeta['PlugInBlacklist'].keys():
			for blitem in blitems:
				if blitem in xprotmeta['PlugInBlacklist']['10'].keys():
					modified = 1
					del xprotmeta['PlugInBlacklist']['10'][blitem]

		if modified != 0:
			self.write_xprotmeta(xprotmeta)

	def flash_plugin_blacklisted(self):
		return self.plugin_blacklist_items_exist([
			'com.macromedia.Flash Player.plugin',
			'com.macromedia.Flash Player ESR.plugin',
			])

	def remove_flash_plugin_blacklist(self):
		self.remove_plugin_blacklist_items([
			'com.macromedia.Flash Player.plugin',
			'com.macromedia.Flash Player ESR.plugin',
			])

	def java_webcomponent_exists(self):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			False

		if 'JavaWebComponentVersionMinimum' in xprotmeta.keys():
			return True

		return False

	def remove_java_webcomponent(self):
		xprotmeta = self.read_xprotmeta()

		if not xprotmeta:
			return

		if 'JavaWebComponentVersionMinimum' in xprotmeta.keys():
			del xprotmeta['JavaWebComponentVersionMinimum']
			self.write_xprotmeta(xprotmeta)

	def java_plugins_blacklisted(self):
		return self.plugin_blacklist_items_exist([
			'com.apple.java.JavaAppletPlugin',
			'com.apple.java.JavaPlugin2_NPAPI',
			'com.oracle.java.JavaAppletPlugin',
			])

	def remove_java_plugins_blacklist(self):
		return self.remove_plugin_blacklist_items([
			'com.apple.java.JavaAppletPlugin',
			'com.apple.java.JavaPlugin2_NPAPI',
			'com.oracle.java.JavaAppletPlugin',
			])
