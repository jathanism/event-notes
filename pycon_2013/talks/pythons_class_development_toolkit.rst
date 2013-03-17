##################################
Python's Class Development Toolkit
##################################

:Date:
    2013-03-16

:Speaker:
    Raymond Hettinger

The Challenge
=============

+ You write a class, test it, DONE.
+ What about how users use it?
+ Every new user will stretch (abuse) your code in ways you never conceived.

Our Plan
========

+ Learn the dev toolkist
+ See how users exercise your code
+ Have fun

Agile vs. Lean
==============

Agile Methodology
-----------------

+ Out with waterfall: design, code, test, ship
+ In with: tight iterations
+ Core idea: iterate and adapt rapidly

Lean Startup Methodology
------------------------

+ Out with: raise capital, spend it, go to market, fail
+ In with: ship early, get feedback, pivot, iterate
+ Agile applied to busines

Start coding
============

+ Start with the documentation
+ Use new-style classes (inherit from object)

  - This is the default in Python 3

+ Variables not unique to instance should not be instance variables
+ ``__init__()`` is not a constructor!

  - Its job is to init intance variables.

+ ``self`` is a convention, use it.
+ Class definition is in itself like a module namespace
+ Pi is not a constant, it's a variable that never changes. (hrm?)
+ YAGNI: You ain't gonna need it!

  - aka don't bog your code down with features you don't even need yet
  - Stay minimal!

+ Shared data should be at class level (class variables)
+ Don't use floats for your version numbers. Strings or tuples, plz.
+ Always use iterators (e.g. xrange) to conserve memory!

  - Stay in L1 cache where possible

+ If you expose an attribute, expect users to all kinds of interesting things
  with it.

  - In Python this is common and normal. Accept it.

+ Adapt init/constructor for commoon use-cases

  - CONSTRUCTOR WARS!

    * e.g. Converter functions passed to init, are bad.
    * Everyone should win.

  - Provider alternate constructors
  - classmethods make for great alternate constructors

    * dict.fromkeys(), datetime.fromtimestamp(), etc.

  - And they should always work from subclasses

+ Always plan for subclassing! (use ``super()``!)
+ Use staticmethods to attach functions to classes

+ Use dunder prefix for class-local variables (e.g. subclasses)
+ Slots save memory, but you lose the ability to inspect, modify

  - Flyweight design pattern
  - Always do them LAST, as a memory efficiency step
  - Cache miss is as expensive as a floating point divide
  - Slots are not inherited by subclasses

The Code
========

.. literalinclude:: circle.py

Summary
=======

1. Always inherit from object
2. Use instance vars for info unique to instances.
3. Use class vars for shared info across instances.
4. Regular (instance) methods need ``self`` to access instance data.
5. Use classmethods for alternative constructors. They need ``cls``.
6. Use staticmethods to attach funcs to classes, They don't need ``self`` or
   ``cls``.
7. ``property()`` lets getter/setters be invoked auomatically w/ attr access
8. ``__slots__`` implements Flyweight Design Pattern by suppressing instance
   dict.
