###################################
Things to Make Writing Tests Easier
###################################

:Date:
    2013-03-16

:Speaker:
    Chris Withers

Something to Test
=================

+ Parsing CSV data
+ tempfile.NamedTemporaryFile

  - Write stuff to it

+ ``python -m unittest discover``

Reduce Boilerplate
==================

+ use ``setUp()`` and ``tearDown()`` (w/ ``unittest.TestCase`` objects)

Libs
====

+ unittest (stdlib)
+ testfixtures
+ mock (hello, again)
+ unittest2

Rich comparisons with testfixtures
==================================

Basic comparisons
-----------------

+ testfixtures.compare

  - Gives you a diff on long strings
  - Displays differences when comparing collections (sets, dicts, etc.)

Generators
----------

+ testfixtures.generator

  - Rich comparison of generators/iterators!
  - Be careful of just comparing by id
  - Be careful when unwinding

Strings
-------

+ testfixtures.StringComparison

  - good for process ids, thread ids
  - Costly (regex): use sparingly 
    
Complex Objects
---------------

+ testfixtures.Comparison

  - Compare objects that don't support comparison (cool?)
  - ``Comparison('module.SomeClass' == SomeClass(1,2)``
  - Useful post-comparison representation
  - You don't have to compare every attribute!

Registering your own comparison objects
---------------------------------------

+ testfixtures.comparison.register
+ testfixtures.comparison.compare_sequence
+ Strict comparison

  - Relaxed and useful by default
  - Not always what oyu want, so you canbe strict (``strict=True``)

+ What about context?

  - No contextual information provided
  - Use the prefix arg:

    * ``compare(1, 2, prefix='this is what happened:')``

Things that print
-----------------

+ Lots of code writes to stdout/stderr
+ We should test that!
+ testfixtures.OutputCapture

  - ``with OutputCapture() as output:``
  - later... ``output.compare(...)``

Exceptions
----------

+ testfixtures.ShouldRaise

  - ``with ShouldRaise(): as s``
  - later... ``compare(s.raised, ...``

Files and Directories
---------------------

+ Annoying to setup
+ Have to clean up
+ Difficult to make x-platform

+ Reading/Writing files

  - textfixtures.TempDirectory
  - ``with TempDirectory() as dir:``
  - ``dir.read()``, ``dir.write()``, ``dir.makedir()``
  - ``dir.check_dir()`` - Check the dir
  - ``dir.check_all()`` - Check contents
  - truly x-platform,

Logging
-------

+ testfixtures.LogCapture
+ Captures logs..
+ ``with LogCapture() as log``
+ later... ``log.check(..)``
+ Capture a certain level, or logger, etc.
+ Uninstall and reinstall to only cap certain code/log events.

Mocking
-------

+ Where do you mock? 
+ testfixtures.Replacer
+ testfixtures.not_there
+ testfixtures.replace

  - Mock all kinds of stuff: dict keys, list elements, object attributes

+ mock.Mock, mock.call

Datetimes
---------

+ testfixtures.test_datetime

  - Supports deltas, timezones
