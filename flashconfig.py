import os

FLASH_PLAYER_CONFIG_FILE='/Library/Application Support/Macromedia/mms.cfg'

class FlashPlayerConfig:
	def exists(self):
		return os.path.exists(FLASH_PLAYER_CONFIG_FILE)

	def read_config(self):
		'''Read config file and return dictionary'''

		if not self.exists():
			return None

		with open(FLASH_PLAYER_CONFIG_FILE, 'r') as f:
			content = f.readlines()

		config_dict = {}

		for l in content:
			nl = l.strip().split('=')
			config_dict[nl[0]] = nl[1]

		return config_dict

	def write_config(self, config_dict):
		'''Writes whole configuration file'''

		config_str = ''

		mydir = os.path.dirname(FLASH_PLAYER_CONFIG_FILE)

		if not os.path.isdir(mydir):
			os.makedirs(mydir)

		for k in config_dict.keys():
			config_str += k + '=' + config_dict[k] + "\n"

		with open(FLASH_PLAYER_CONFIG_FILE, 'w') as f:
			f.write(config_str)

	def auto_updates_disabled(self):
		config = self.read_config()

		if not config:
			return False

		if config.get('SilentAutoUpdateEnable') == '0' and config.get('AutoUpdateDisable') == '1':
			return True

		return False

	def disable_auto_updates(self):
		config = self.read_config()

		if not config:
			config = {}

		config['SilentAutoUpdateEnable'] = '0'
		config['AutoUpdateDisable'] = '1'

		self.write_config(config)

