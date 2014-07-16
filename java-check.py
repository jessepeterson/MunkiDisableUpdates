import sys

if 'AppleXProtectMeta' not in locals().keys():
	# import if not running in concatenated script
	from xprotmeta import AppleXProtectMeta
	from javadeployment import JavaDeploymentConfigFile, JavaDeploymentPropertiesFile

xpm = AppleXProtectMeta()
jdc = JavaDeploymentConfigFile()
jdp = JavaDeploymentPropertiesFile()

if xpm.java_plugins_blacklisted():
	print 'Java plugins are blacklisted; returning 0 (not installed)'
	sys.exit(0)

if xpm.java_webcomponent_exists():
	print 'Java web component version exists; returning 0 (not installed)'
	sys.exit(0)

if not jdc.deployment_properties():
	print 'Java deploy config: prop not configured; returning 0 (not installed)'
	sys.exit(0)

if not jdc.deployment_properties_mandatory():
	print 'Java deploy config: prop mandatory not configured; returning 0 (not installed)'
	sys.exit(0)

if not jdp.expiration_check_disabled():
	print 'Java deploy prop: expiration check not disabled; returning 0 (not installed)'
	sys.exit(0)

if not jdp.expiration_check_locked():
	print 'Java deploy prop: expiration check not locked; returning 0 (not installed)'
	sys.exit(0)

print 'Java not blacklisted and no web component version; returning 1 (installed)'
sys.exit(1)
