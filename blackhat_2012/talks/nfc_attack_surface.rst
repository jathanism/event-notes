==============================
Analysis of NFC Attack Surface
==============================

:Date:
    2012-07-25

:Speakers:
    Charlie Miller

:Slides:
    http://media.blackhat.com/bh-us-12/Briefings/C_Miller/BH_US_12_Miller_NFC_attack_surface_Slides.pdf

The Gist
========

+ Fuzzing NFC stacks
+ Potential attacks and demos
+ Many Android phones have NFC. Not iPhone yet.
+ He broke into a Google Nexus S and Nokia N9 using NFC!

Motivation
==========

+ NFC coming to a phone near you!
+ "Server-side" attack vector
+ Very hard to test NFC implementations

NFC Attack Surface
==================

+ New way to test NFC stacks
+ Examples

  - Google wallt PIN brute force
  - parking meters
  - bus passes, gym memberships
  - URL spoofing, vending machines

NFC Basics
==========

+ Based on RFID (ISO 14443)
+ 13.56 MHz (+/- 7kHz)
+ Range: < 4cm
+ Data rates: 106, 212, 424 kbps
+ Typically on when phone screen is on (not when "asleep")
+ Modes: Passive, Active (P2P)
