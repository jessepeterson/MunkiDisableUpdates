import plistlib
import os

JAVA_SYSPREF_PLIST = '/Library/Preferences/com.oracle.java.Java-Updater.plist'

class JavaUpdaterPref:
	def exists(self):
		return os.path.exists(JAVA_SYSPREF_PLIST)

	def read(self):
		if not self.exists():
			return None

		return plistlib.readPlist(JAVA_SYSPREF_PLIST)

	def write(self, config_dict):
		plistlib.writePlist(config_dict, JAVA_SYSPREF_PLIST)

	def updates_disabled(self):
		config_dict = self.read()

		if not config_dict:
			return False

		if 'JavaAutoUpdateEnabled' in config_dict.keys() and not config_dict['JavaAutoUpdateEnabled']:
			return True
		else:
			return False

	def disable_updates(self):
		config_dict = self.read()

		if not config_dict:
			config_dict = {}


		config_dict['JavaAutoUpdateEnabled'] = False

		self.write(config_dict)
