################
Python Profiling
################

:Date:
    2013-03-15

:Speaker:
    Amjith Ramanujam
    
What is it?
===========

+ This is nothing like racial profiling
+ All about measuring performance

cProfile
========

+ The jam, part of the standard library
+ ``python -m cProfile lcm.py``
+ Dump to a .pstats file

GUI Profiler: RunSnakeRun
-------------------------

+ Makes pretty square maps of stuff
+ Sort by column, drill down, awesome.

Tips
----

+ Huge overhead
+ "Don't run in production!"
+ Slow
+ Not realistic

Targeted Profiling
==================

+ Critical functions
+ Start profiler, profile critical thing, stop profiler
+ ``from profile_func import profile_func``::

    @profile_func
    def lcm(arg1, arg2):
        # ...

+ You don't want to affect your critical function!
+ Pros: less overhead, finer resolution
+ Cons: still slow, manual, littering code w/ decorators

New Relic
---------

+ Targeted, hybrid profiling
+ Web apps only :/
+ (They don't use cProfile)
+ Targeted profiling:

  - Web frameworks (django, etc)
  - View handlers
  - SQL calls
  - Monkey patch calls you care about

Hybrid profiling
================

+ Top-level function only
+ Timing data
+ Capture args
+ Waterfall diagram/graphing
+ Pros: fast, function args
+ Cons: semi-manual, limited instrumentation

Statistical Profiling
=====================

+ Non-deterministic
+ Kind of like overly-attached girlfriend
+ Interrupt, inquire, collate = OVERLY ATTACHED

  - Who are you with
  - Where are you
  - When are you coming home?
  - I miss you!

+ Interrupt (timer):

  - UNIX signals
  - Threads

+ Inquire (trace)

  - Stack frame of every thread
  - import sys, traceback

    * frames = sys._current_frames()
    * traceback.extract_stack(frame)

+ 3rd party libs

  - StatProf (UNIX signals, CLI)
  - PLOP (Unix Signals, D3 Call Graph), by DropBox

    * Size of the bubble indicates CPU time

  - New Relic (threads, GUI)

X-Ray Sessions
==============

+ New Relic SECRET BETA (until now)
+ Deterministic
+ Targeted transactions (e.g. checkout page), count, gather, profile threads
+ Measure/graph the response & throughput
+ PROFILE ALL THE THINGS
