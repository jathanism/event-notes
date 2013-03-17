###############################################################
Dynamic Code Patterns: Extending Your Applications with Plugins
###############################################################

:Date:
    2013-03-16

:Speaker:
    Doug Hellman

The Gist
========

+ Comparison of dynamic code loading in various projects

What's a Plugin?
================

+ Loaded dynamically
+ Extends core
+ Possibly (usually) unknown source

Why Plugins?
============

+ Better API abstraction
+ Separate between core + extensions
+ Reduce core deps.
+ Strategy Pattern vs. Visitor Pattern

  - e.g. Device drivers

+ Indirect code contributions

Ceilometer
==========

+ Metering component for OpenStack
+ Measuring clouds, Billing
+ Extend/customize by deployers
+ Components communicate using notification message bus 

  - Meter data has event listener on master message bus
+ Plugin types

  - message bus
  - reciving notif
  - polling
  - storage

Research
========

+ Sphinx
+ Django
+ Pyramid
+ Mercurial
+ Nose
+ Trac
+ SQLAlchemy
+ Nova - primary component for OpenStack
+ cliff - Speaker wrote this (sub-commands for main app)
+ virtualenvwrapper - Speaker wrote this too :)

Discovery
---------

+ Explicit vs. Implicit
+ Import reference vs. File

Enabling
--------

+ Explicit vs. Implicit

Importing
---------

+ Custom 

  - Django, Sphinx
  - This is prone to errors

+ pkg_resources

  - cliff, virtualenvwrapper
  - This is saver

Integration
-----------

+ Prompt vs. Inpsect
+ Granularity: Fine vs. Coarse

  - Fine: single class or function
  - Coarse: Single plugin might include hooks into multiple parts of app

    * Django is coarse

API Enforcement
---------------

+ Convention vs. Base Class/Interface

  - Convention: Django
  - Class: cliff (abc), Trace (zope.interface)
  - Duck-typing probably a good idea for classes

Invocation
----------

+ Driver: Per use-case
+ Dispatcher: slkk;ds
+ Iterator: All data is given to all plugins

Designing a Plugin
==================

Discovery/Importing
-------------------

+ Think about entry points
+ Consider distribute and pkg_resources
+ Be consistent!

Decisions made in Ceilometer
----------------------------


Enabling
~~~~~~~~

+ Explicit disabling (e.g. config file)
+ Automatic disabling

Integration
~~~~~~~~~~~

+ Fine
+ Inspect
+ App owns relationship

API Enforcement
~~~~~~~~~~~~~~~

+ Abstract Base Classes
+ Duck typing

Invocation
~~~~~~~~~~

+ storage: river
+ notif: dispather
+ pollsters: iterators

stevedore
=========

+ Download: https://github.com/dreamhost/stevedore

  - Docs: http://stevedore.readthedocs.org/en/latest/

+ Plugin lib that you should use!!
+ Implements plugin patterns
+ Wraps pkg_resources
+ NamedExtensionManager

  - multple plugins
  - only loads named plugins
  - map() them

+ EnabledExtensionManager

  - multiple lugins
  - cheakcs each w/ func on load
  - map() them

+ DispatchExtensionManager

  - multple plguins
  - invokes subset on map()

+ DriverManager

  - single plugin
  - direct access
