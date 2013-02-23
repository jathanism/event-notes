=======================
The Secure Boot Journey
=======================

:Speaker:
    Matthew Garrett

:Date:
    2013-02-23

The Past
========

+ UEFI is cross-vendor ($3000/year to contrib)
+ 2006: UEFI 2.0 - describes method for signing drivers
+ 2008: UEFI 2.2 - describes method for image validation
+ 2011: Windows 8 client hardware must default ot enforcing UEFI Secure Boot.

  - WTF MSFT?!
  - Will this mean that ONLY Windows 8 can run?

UEFI Secure Boot
================

+ Hash a binary
+ Sign it with private key
+ On bot, check hash
+ Check sig was made w/ trusted key
+ Refuse to boot if checks fail

But why?
--------

+ If you hijack the bootloader, you get total control.
+ Perfectly designed malware could be virtually impossible to detect
+ Command & control == Profit
+ Therefore: Anti-terrorism (Obviously)

What are our options?
=====================

+ Drink
+ No, really. Drink.
+ Break RSA, taking down SSL with it.
+ Ok, back to drinking.

Cause Trouble
-------------

+ Sept 2011: Matthew blogs about the Win8 requirements (aka WTF MSFT?!)
+ PANIC
+ It's easy to cause trouble:

  - Just tell people Microsoft is trying to take Linux away from you.

+ 2 days later, MSFT responds:

  - "Secure Boot is a UEFI standard, not a Windows 8 feature."
  - Translation: Blame the system vendors (yeah, right)

+ Bullets are also "standards"

  - Aren't you glad you're being shot at with a standard?

Now What?
=========

+ Don't just run around: Run around and scream.
+ Try to convince vendors to ship a Linux key?

  - Who would control it?
  - Whould get access to it?
  - What baout licensing implications of shipping objects signed with it?

+ What if there was a Red Hat key? 

  - What about the PR issues?
  - What about Debian, Ubuntu, etc...

+ Can we get aaccess to MSFT key? (Heh.)

Other options
-------------

+ Can we avoid pre-instaled keys entirely?
+ What about installing a new signing key when you install the OS?
+ Give up this Linux thing, take up goat farming.

December 2012
=============

+ Vendors must provide a mechanism to disable Secure Boot
+ Vendors must provide a mechanism for users to install their own keys

Did we win?
-----------

+ No standard way of key mgmt
+ No standard way of disabling Secure Boot
+ No way of remote deployments
+ Complexity & documentation nightmare
  - how do you get end-users to do this themselves?

Mcirosft Plays Ball

+ Commtited to provide open access ot the UEFI signing service
+ Sigs are contingent upon not being used to attack Windows (Derp)
+ Potential revocatoin of existing sigs  (e.g. Red Hat key exploited to attack)

Licenese
========

+ "Everyone knows" GPLv3 requires you to release signing keys
+ GPLv3 material must be configurable by the end-user.
+ (Everyone is wrong)

Two Getouts
-----------

+ If it's possible to replace it, you don't need to ship the keys
+ If it's not a User Product, you don't need to ship the keys
+ (Software isn't a User Product, e.g. a physical object)

User Control
============

+ User freedom is essential
+ Users need key mgmt
+ Machine Operator Key

  - variables can be limited ot pre-boot
  - keys stored in them can't nbe modified by the OS
  - key install can be limited to physically presetn users
  - code written and contributed by Suse

Secure Boot Support

+ Ubuntu 12.10 and 12.04.2
+ Fedora 18
+ A few smaller distros.

Pre-signed Shim
---------------

+ Signed binary w/ no intrinsic trust
+ Insall distro key as first step of install process
+ NO MST!!
+ No risk of revocation

Now what?
=========

+ Linux can be installed w/out disabling Secure Boot or changing firmware
  settings
+ Users can install and manage their own keys
