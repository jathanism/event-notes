##################################
logstash - Open Source Log Parsing
##################################

:Speaker:
    Jordan Sissel

:Date:
    2013-02-24

:Site:
    http://logstash.net

:Blog:
    http://sysadvent.blopgspot.com

Why
===

+ Mascot is a log with a mustache!
+ Because logging sucks.
+ You wrote some crazy-ass regex and now you're covered in birds

+ Other options:

  - graylog2
  - flume
  - storm
  - elsa

+ Distributed as a Jar, written in Java.

Case Study: Email
=================

Old Solution
------------

- reduced support per bad tooling

New Solution
------------

+ Central logstash cluster
+ One web search interface
+ Faster, better, etc, etc. 

Implementation
--------------

+ Logging agent running on systems
+ 7-node logstash/elasticsearch cluster
+ Stats

  - 4TB * 7 
  - 500M ev/day
  - ~10k events/sec
  - 4 B ev/wek
  - 1/TB/wk
  - 10% peak CPU

How can it help you?
====================

+ powerful, flexible
+ search, anyalytics
+ integrates well
+ logstash is a pipe for events (a timestamp and some data)

Inputs
------

+ Where logs come from 
+ 30 formats supported today
+ gemfire, redis, logs, files, etc, etc.

Filters
-------

+ 25 built-in filters
+ grok: "Describe the shape of your events" (key/value pairs)
+ date: THEY ARE ALWAYS DIFFRENT FORMATS
+ geoip: "Where is 24.22.31.135?"
+ anonymize: Sanitize PII from logs
+ complex: k/v-pairs, json, xml, csv, url, multi-line
+ mutate: modify events (like sed)
+ translate: map values (301 -> "Redirect Permanent")

Outputs
-------

+ ElasticSearch
+ Graphite
+ Pagerduty
+ Redis, ZMQ, RabbitMQ, STOMP, XMPP, IRC... WHATEVER YOU WANT

Principles
==========

+ If a newbie ahs a bad time, it is a bug.
+ Make it possible, make it correct, make it fast. In that order.
+ Open Source: APL 2.0.
+ Should be easy to integrate.

Extensions
==========

+ Kibana: Recommened web-interface - Flippin' awesome.
+ logstash-cli: CLI interface... :P
+ cookbook.logstash.net: Useful patterns and docs
