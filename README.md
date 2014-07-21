Scripts to assemble pkginfo files that disable auto-updates and version blocks for various software.

Simply execute `./assemble.sh` to generate.

Currently supported:

* Adobe Flash Player (`AdobeFlashPlayerUpdateDisable-0.X.X.pkginfo`)
  * Disables auto-updates (mms.cfg)
  * Removes blocked plugin entries from Apple's XProtect meta plist
* Oracle Java 7 (`JavaUpdatesDisable-0.X.X.pkginfo`)
  * Disables auto-updates (deployment.properties, deployment.config)
  * Removes blocked plugin entries from Apple's XProtect meta plist
  * Removes Java web component minimum version from Apple's XProtect meta plist
* Adobe Reader (`AdobeReaderUpdateDisable-0.X.X.pkginfo`)
  * Disables auto-updates (FeatureLockdown:bUpdater in system preference)
* OS X (`OSXUpdatesDisable-0.X.X.pkginfo`)
  * Disables OS X software update schedule (`/usr/sbin/softwareupdate`)
  * For 10.6 through 10.8 unloads the XProtect meta launch daemon
