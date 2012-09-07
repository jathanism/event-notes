=====================================
Passive Bluetooth Monitoring in Scapy
=====================================

:Date:
    2012-07-26

:Speaker:
    Ryan Holeman

:Slides:
    http://hackgnar.com/article/slides-libraries-and-tutorials-my-defcon-and-black/

The Gist
========

+ scapy-btbb - Open source Bluetooth scanner
+ Bluetooth is a frequency-hopping protocol

BTBB
====

+ BTBB = Bluetooth Baseband
+ Everyday devices cannot acess the baseband

Address Parts
=============

+ NAP - Non-significant Address Parts
+ UAP - Upper Address Parts
+ LAP - Lower Address Parts

+-------+-----+----------+
|  NAP  | UAP |    LAP   |
+-------+-----+----------+
| AA:BB | CC  | DD:EE:FF |
+-------+-----+----------+

Tools
=====

+ BTBB hardware: Ubertooth 

  + Kismet plugin: dump BT to pcap!!

+ libbtbb - Wireshark plugin

Goal
====

Get BTBB into Python

+ btbb layer in Scapy
+ load BT pcap into PcapReader
+ read pcap files as they are written
+ vendor/metadata support (resolution)
+ Use iPython w/ iPython Notebook (!!)
+ Pandas for graphing/plotting
