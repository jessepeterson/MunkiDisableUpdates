import sys

if 'AppleXProtectMeta' not in locals().keys():
	# import if not running in concatenated script
	from xprotmeta import AppleXProtectMeta
	from javadeployment import JavaDeploymentConfigFile, JavaDeploymentPropertiesFile

xpm = AppleXProtectMeta()
jdc = JavaDeploymentConfigFile()
jdp = JavaDeploymentPropertiesFile()
jup = JavaUpdaterPref()

print 'Removing Java XProtect blacklist'
xpm.remove_java_plugins_blacklist()

print 'Removing Java web component version'
xpm.remove_java_webcomponent()

print 'Writing Java deployment config'
jdc.write_disabled_update_config()

print 'Writing Java deployment properties'
jdp.write_disabled_update_config()

print 'Disabling Java Upadter preference'
jup.disable_updates()

sys.exit(0)
