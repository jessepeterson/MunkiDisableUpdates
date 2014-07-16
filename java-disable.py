import sys

if 'AppleXProtectMeta' not in locals().keys():
	# import if not running in concatenated script
	from xprotmeta import AppleXProtectMeta
	from javadeployment import JavaDeploymentConfigFile, JavaDeploymentPropertiesFile

xpm = AppleXProtectMeta()
jdc = JavaDeploymentConfigFile()
jdp = JavaDeploymentPropertiesFile()

print 'Removing Flash player blacklist'
xpm.remove_java_plugins_blacklist()

print 'Removing Java web component version'
xpm.remove_java_webcomponent()

print 'Writing Java deployment config'
jdc.write_disabled_update_config()

print 'Writing Java deployment properties'
jdp.write_disabled_update_config()

sys.exit(0)
