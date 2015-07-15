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

JAVA_DEPLOY_PLIST = '/Library/Preferences/com.oracle.javadeployment.plist'

class JavaDeployPref:
	def exists(self):
		return os.path.exists(JAVA_DEPLOY_PLIST)

	def read(self):
		if not self.exists():
			return None

		return plistlib.readPlist(JAVA_DEPLOY_PLIST)

	def write(self, config_dict):
		plistlib.writePlist(config_dict, JAVA_DEPLOY_PLIST)

	def updates_disabled(self):
		config_dict = self.read()

		if not config_dict:
			return False

		if '/com/oracle/javadeployment/' in config_dict.keys() \
		        and 'deployment.macosx.check.update' in config_dict['/com/oracle/javadeployment/'] \
		        and not config_dict['/com/oracle/javadeployment/']['deployment.macosx.check.update']:
			return True
		else:
			return False

	def disable_updates(self):
		config_dict = self.read()

		if not config_dict:
			config_dict = {}

		if '/com/oracle/javadeployment/' not in config_dict.keys():
			config_dict['/com/oracle/javadeployment/'] = {}

		config_dict['/com/oracle/javadeployment/']['deployment.macosx.check.update'] = False

		self.write(config_dict)
