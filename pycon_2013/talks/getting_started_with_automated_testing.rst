######################################
Getting Started with Automated Testing
######################################

:Date:
    2013-03-16

:Speaker:
    Carl Meyer

:Slides:
    http://oddbird.net/start-testing-preso
    
What is it?
===========

+ Untested code is legacy code
+ This guy LOVES to test!
+ Even the slides have tests! Whoa, man.

Let's Make a Thing!
===================

Git recommendations engine
--------------------------

+ gitrecs.py

  - similarity() - Return similarity score for two users

+ Testing things manually gets old fast.

  - Updating your tests with your revisions gets older faster.
  - Repetitive and boring... Therefore you skip them.
  - Not easily-reproducable
  - Error-prone

+ ... And you ship broken code because it's not fully tested

Automate a test!
----------------

+ test_gitrecs.py

  - from gitrecs import similarity

+ ``assert similarity(blah1, blah2) == expected_value``
+ Got ZeroDivisionError

  - New test: ``assert similarity({}, {}) == 0.0``

+ pytest - Test runner

  - Knows how to discover & run test (if name is ``test_foo.py``

Test runners
============

+ py.test
+ Nose
+ unittest (stdlib)
+ twisted.trial
+ zope.testrunner

Why Tests?
==========

+ So you knw when your code is broken.
+ Help later devs grok your code.
+ Improve the design of your code.
+ Testing things that rely on network information is hard

  - You must fake it! (Mock objects with boilerplated data?)
  - These tests are less clear
  
+ Testable code is maintainable

  - The less a function knows about the world... 
  - The more robust it is against changes
  - See: Principal of Least Knowledge
  - Therefore: The less of the world you have to setup to test it

Types of Tests
==============

+ Doctest is not recommended

  - Fragile
  - No isolation
  - Harder to maintain
  - Good for testing your documentation, but that's it!

Unit Tests
----------

+ Test one "unit" of code (func/method)
+ Small & fast
+ Focused: Informative failures
+ Con: Require more refactoring w/ changes:w

Integration Tests
-----------------

+ Test that components talk to each other correctly
+ Slower, exercises more code.
+ "Black box" tests aka "system", "functional", or "acceptance" tests.

Workflows for Testing
=====================

+ Make it a habit, not a chore.
+ Testing first is more fun (objective!)

Adding a feature
----------------

+ Write an end-to-end test describing the working feature.
+ Start implementation from the outside in.
+ Program by wish: "I wish I had a thing that did..."

  - Stub it.

+ For each stubbed func write tests describing how it *should* work.

The "spike" workflow
--------------------

+ Write exploratory code to figure out a problem
+ Strict TDD says delete your spikes and rewrite them test-first...
+ Try it... It can be illuminating.

Retrofitting workflow
---------------------

+ Codebase with out test? (*cough* `Trigger <https://trigger.rtfd.org>`_)

  - Probably not structured for tests. Oh, bother.

+ Start /w system tests.
+ Use code coverage as a metric for testable areas.

  - ``pip install coverage``

See Also
========

+ tox - test your lib accross multiple Python versions/configs
+ mock - easily create fakes for testing (included in Python 3.3)
+ WebTest - request/response for WSGI apps
+ Selenium - browser automation
+ http://pytest.org

Coding with Tests
=================

+ Fun and satisfying!
+ Replaces fear w/ moxy.
+ Results in better code.
