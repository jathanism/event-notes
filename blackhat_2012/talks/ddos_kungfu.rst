========================================
DDoS Black and White "Kung Fu" Revealead
========================================

:Date:
    2012-07-28

:Speakers:
    Tony Miu, Anthony Lai, &c;

:Slides:
    https://media.defcon.org/dc-20/presentations/Lai-Miu-Wong-Chung/DEFCON-20-Lai-Miu-Wong-Chung-DDoS-Kungfu.pdf

How to DDoS a Site
==================

+ Analyze web apps for high-cost methods (GET vs. POST)
+ Calculations of resources w/ high cost, esp. db ops, large files
+ Test for Referer, Keep-Alive, Pipelining
+ Force to not load from e.g. (e.g. /uri/?foo)
+ Spoof Content-Length, set to irregular value
+ Focus on TCP & HTTP (TCP x HTTP killer)
+ Focus on TCP *state*
+ Use HTTP as example to control TCP state

  - Server reserves resources to control TCP state
  - Focus on reply of server: FINACK, RST, HTTP 302, etc.

Target TCP States
=================

+-------------+---------------+
| TCP State   | Defense       |
+-------------+---------------+
| established | lower timeout | 
+-------------+---------------+
| FIN_WAIT_1  | RST timeouts  |
+-------------+---------------+
| CLOSE_WAIT  | TCP timeouts  |
+-------------+---------------+
