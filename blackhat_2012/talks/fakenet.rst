=======
FakeNet
=======

:Date:
    2012-07-26

:Speaker:
    Andrew Honig

:Link:
    http://practicalmalwareanalysis.com/fakenet/

The Gist
========

+ Fakethat is intended to run on Windows XP.
+ Allows you to hijack all socket connections received by the system
+ Has an embedded Python 2.7.3 interpreter (custom modules!!)
+ Feasible for a single-system dummy test network.

Caveats
=======

+ Custom socket I/O; _socket.so module was intentionally excluded
+ In order to do socket calls you must import FakeNet.
+ Greatly simplified interface, handles buildup/teardown of session
+ You worry about send/recv only
