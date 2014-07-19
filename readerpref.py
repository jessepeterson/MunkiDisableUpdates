import plistlib
import os

READER_SYSPREF_PLIST = '/Library/Preferences/com.adobe.Reader.plist'
# READER_SYSPREF_PLIST = '/tmp/com.adobe.Reader.plist'

class AdobeReaderPref:
	def exists(self):
		return os.path.exists(READER_SYSPREF_PLIST)

	def read(self):
		if not self.exists():
			return None

		return plistlib.readPlist(READER_SYSPREF_PLIST)

	def write(self, config_dict):
		plistlib.writePlist(config_dict, READER_SYSPREF_PLIST)

	def updates_disabled(self, versions=['10', '11']):
		config_dict = self.read()

		if not config_dict:
			return False

		for v in versions:
			if not v in config_dict.keys():
				return False

			if 'FeatureLockdown' not in config_dict[v].keys():
				return False

			if 'bUpdater' not in config_dict[v]['FeatureLockdown'].keys():
				return False

			if config_dict[v]['FeatureLockdown']['bUpdater'] != False:
				return False

		return True

	def disable_updates(self, versions=['10', '11']):
		config_dict = self.read()

		if not config_dict:
			config_dict = {}

		for v in versions:
			if not v in config_dict.keys():
				config_dict[v] = {}

			if 'FeatureLockdown' not in config_dict[v].keys():
				config_dict[v]['FeatureLockdown'] = {}

			config_dict[v]['FeatureLockdown']['bUpdater'] = False

		self.write(config_dict)
