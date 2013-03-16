###################
Let Them Configure!
###################

:Date:
    2013-03-16

:Speaker:
    Lukasz Langa

A Sermon on Reusability
=======================

+ Let's talk about cars.
+ Cars break easily.
+ They require special tools.
+ Standard tool: "English key" aka crescent wrench

  - A highly-configurable tool

Four Desirable Characteristics of Configuration
===============================================

1. Composability

   - Operating system configuration

     * user defaults, system defaults, runtime defaults, etc.

2. Readability

   - By humans AND computers
   - To know when an option is toggled

3. Exchangeability

   - Program can write changes back

4. Discoverability

   - Self-documenting
   - Easy to use

World Tour
==========

.ini format
-----------

+ Not really a standard; informatl standard
+ Implementations vary (white space, blank lines, etc.)
+ Status:

  - Composable? Highly!
  - Readable? If you're consistent
  - Exchangable? If you keep the encoding the same
  - Discoverable? Mostly, depending on developer

Custom formats
--------------

+ Apache: Confusing, not the most readable
+ Nginx: Kind of c-like (braces), supports nesting, context, scriptable

JSON
----

+ Wasn't designed to be a config format
+ It's a transmission format
+ Simple, human-readable, unicode, x-platform
+ No includes, no cascading, must not output comments

TOML? 
-----

+ New kid on the block
+ By Tom from GitHub (which may lend to popularity)

  - http://github.com/mojombo/toml

+ Like ini, but supports cascading/nesting
+ Inline comments, datetimes, integers, lists, booleans 
+ Strings should be UTF-8, single-line and double-quoted

Complex formats
---------------

+ XML :(

  - Schema validation
  - Not human-readable

+ YAML

  - Actually a transmissoin format
  - Lends itself well to configuration
  - Superest of JSON, has native data types/structures

    * Lends itself to security problems :(

  - Not very extensible, very complicated

    * YAML spec is 80 pgs long

  - Significant whitespace is fragile for configuration

+ So what about Python?

  - UNLIMITED POWER!!
  - Problematic if user is not a programmer (a contrived problem IMO)

Awkward formats
---------------

+ DSLs, such as "plain language" formats
+ Prone to strange complexity, bugs
+ SQLite

  - Postfix can use SQLite databases instead of strings
  - Mongrel2 stores all config using SQLite
  - Ensures only programmers would be able to config your app

+ Windows Registry (the horror)

  - Not exchangeable
  - Windows only
  - User vs. program settings is... difficult
  - Single point of failure
  - "kind of" readable
  - Only format that feeds an economy to clean it up

Worst format ever
=================

+ The one you made up yourself
+ You impose a learning curve on your users
+ Your design decisions will be unintuitive
+ You will fail at parsing!
+ Configuration written once has to be supported forever!

How much configuration do you want?
===================================

+ One-size fits all 
+ Dropbox has very weird server-side config
+ Config != Data

  - Config: Describes behavior
  - Code: Defines and executes behavior
  - Data: Subject to behavior

+ Hard-coding is an anti-pattern

  - Embedding source-code in configuration is too

Practical Configurability
=========================

Django!
-------

+ Django mixes different kinds of settings

  - Framework behavior
  - App behavior
  - Deployment settings

+ Using ``execfile()`` for config includes?
+ Class-based configuratoin templates (e.g. dev, prod, caching)
+ .ini configuration for heirarchial configs

File-based configs
------------------

+ Use configglue
+ ConfArgParse
+ Configopt
+ Python 3's new ConfigParser

  - Dictionary-like API
  - Fetch config from dict
  - Highly-customizable!
  - Stuck on Python 2.6? ``pip install configparser``
