=======================
Hacking with WebSockets
=======================

:Date:
    2012-07-26

:Speakers:
    Mike Shema, Sergey Shekyan, Vaagn Toukharian

:Slides:
    http://media.blackhat.com/bh-us-12/Briefings/Shekyan/BH_US_12_Shekyan_Toukharian_Hacking_Websocket_Slides.pdf

The Gist
========

+ "Behold the bi-directional browser"
+ 2-way comm
+ Untrusted code
+ Forcing persistence on a non-persistent protocol!
+ RFC 6455
+ Tunnel arbitrary data (JSON, XML, HTML, images, video, sound... ANOTHER PROTOCOL)

WebSocket Emulation
===================

+ web-socket.js - Flash raw sockets with Flash "security"
+ sockjs-client - Pure JS
+ Force HTML5 in non-HTML5 browser

Why Worry!
==========

+ 0.15% of sites today use WebSockets
+ Most are for support chat (95%)
+ Among remaining 5%, < 1% using crypto
+ OLD THREATS (DoS, MitM)
