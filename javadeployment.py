import os

class JavaDeploymentFile:
	def exists(self):
		return os.path.exists(self.filename)

	def read(self):
		if not self.exists():
			return None

		with open(self.filename, 'r') as f:
			content = f.readlines()

		config_dict = {}

		# TODO: use strpos and string arrays (in case multiple ='s)
		for l in content:
			nl = l.strip().split('=')
			config_dict[nl[0]] = nl[1]

		return config_dict

	def write(self, config_dict):
		config_str = ''

		for k in config_dict.keys():
			config_str += k + '=' + config_dict[k] + "\n"

		mydir = os.path.dirname(self.filename)

		if not os.path.isdir(mydir):
			os.makedirs(mydir)

		with open(self.filename, 'w') as f:
			f.write(config_str)

	def prop_exists_and_matches(self, propname, value):
		config_dict = self.read()

		if not config_dict:
			return False

		if propname in config_dict and config_dict[propname] == value:
			return True

		return False

DEPLOY_PROPERTY_FILE = '/Library/Application Support/Oracle/Java/Deployment/deployment.properties'
# DEPLOY_PROPERTY_FILE = '/tmp/deployment.properties'

class JavaDeploymentConfigFile(JavaDeploymentFile):
	filename = '/Library/Application Support/Oracle/Java/Deployment/deployment.config'
	# filename = '/tmp/deployment.config'

	def deployment_properties(self):
		deploy_prop_url = 'file://' + DEPLOY_PROPERTY_FILE
		return self.prop_exists_and_matches('deployment.system.config', deploy_prop_url)

	def deployment_properties_mandatory(self):
		return self.prop_exists_and_matches('deployment.system.config.mandatory', 'true')

	def write_disabled_update_config(self):
		config_dict = self.read()

		if not config_dict:
			config_dict = {}

		deploy_prop_url = 'file://' + DEPLOY_PROPERTY_FILE

		config_dict['deployment.system.config'] = deploy_prop_url
		config_dict['deployment.system.config.mandatory'] = 'true'

		self.write(config_dict)

class JavaDeploymentPropertiesFile(JavaDeploymentFile):
	filename = DEPLOY_PROPERTY_FILE

	def expiration_check_disabled(self):
		return self.prop_exists_and_matches('deployment.expiration.check.enabled', 'false')

	def expiration_check_locked(self):
		return self.prop_exists_and_matches('deployment.expiration.check.enabled.locked', 'true')

	def write_disabled_update_config(self):
		config_dict = self.read()

		if not config_dict:
			config_dict = {}

		config_dict['deployment.expiration.check.enabled'] = 'false'
		config_dict['deployment.expiration.check.enabled.locked'] = 'true'

		self.write(config_dict)
