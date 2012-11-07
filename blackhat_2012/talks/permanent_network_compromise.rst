=======================================
A Plan for Permanent Network Compromise
=======================================

:Date:
    2012-07-28

:Speakers:
    Phil Purviance, Josh Brashars

:Slides:
    http://media.blackhat.com/bh-us-12/Briefings/Purviance/BH_US_12_Purviance_Blended_Threats_Slides.pdf

Browser-Based Attacks
=====================

Old Skool
---------

+ Exploit Windows
+ Exfiltrate data
+ Detected/removed by AV

Nu Skool
--------

+ aka "Blended threats"
+ multiple vectors (worm gets email, back-door for infection)
+ Break free of the browser and into the network


Why Attack Network Devices?
===========================

+ Hard to detect w/ AV
+ Non-standard upgrade model
+ Ignored by users if service keeps running

Compromising Network Devices
============================

+ Rogue SOHO/wifi routers (!!)

  - More common than you think
  - Engineers, careless QA plugging into Enterprise
  - Default settings!!

+ Bridging enterprise via VPN from compromised home users (!!)
+ Worst case scenario:

  - Make browser do as much as possible
  - Make end-user do all the work

+ Proof-of-concept: 1 JavaScript program

  - Hijack ad networks, upload sites, online surveys
  - Social network sites
  - Exploiting non-technical friends/family with spam posts

Network Scanning w/ JS
======================

+ JSScan
+ JS-Recon
+ jslanscanner
+ Enumerate IP addreses/ports with dynamic element creation (to load an image)
  - code makes a request on the LAN to see if reachable
+ WebSockets
+ Pwning SOHO/home routers w/ default credentials
+ HTTP Basic Authentication
