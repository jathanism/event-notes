##################################################
Transforming Code into Beautiful, Idiomatic Python
##################################################

:Date:
    2013-03-15

:Speaker:
    Raymond Hettinger

:Slides:
    tbd
    
The Gist
=====

+ "Don't do this, do this instead."
+ "Everywhere you see this, replace it with this."
+ Replace all examples in these slides in your real code. Do it.

Replace things..
================

+ Replace index manip with core looping idioms
+ Use for..else and two arg form of iter()

Looping
-------

+ Use xrange vs. range; Python 3: range IS xrange
+ Use enumerate() instead of range(len(iterable)) for indices
+ To loop backwards use reversed(iterable)
+ Use zip to loop over 2 collections

  - Use itertools.izip for large collections (or just default to it)

+ Use sorted(iterable) to loop in order
+ To loop until sential match, use iter(iterable, sentinel)
+ Track multiple exit points, use for..else vs. match + break

Dictionary skills
=================

+ Fundamental Python skill 
+ Linking, counting, grouping
+ Construct a dict from pairs using zip/izip, pass it to dict()
+ Count with a dict: 

  - collections.defaultdict
  - collections.Counter

+ Group with dicts: 

  - dict.setdefault:  ``d.setdefault(key, []).append(name)``
  - collections.defaultdict(list)

+ Is dict.popitem() atomic?

  - Yes. It's thread-safe!!

+ Linking dicts::
  
    defaults = {'a': 1, 'b': 2}
    d = defaults.copy)(
    d.update(os.environ)
    d.update(cli_args)

  - Python3 : ChainMap(cli_args, os.environ, defaults)

Improving Clarity
=================
  
+ Clarify func calls w/ kwargs

  - hours of programmer time > microseconds of performance

+ Everywhere you use tuples use collections.namedtuple instead
+ Use sequence unpacking instead of indexing!
+ Use tuple packing/unpacking for multiple variables (state, assignment in one)

  - ``x, y = 0, 1`` vs. ``x = 0; y = 1``
  - Simultaneous state updates!

Efficiency
==========


+ Don't use + to concatenate, use .join()
+ Don't use  pop, insert, del to update lists; use collections.deque

Decorators & Context Managers
=============================

+ Separate business logic from admin logic

  - business: Open URL, return page
  - admin logic: cache lookup
  - from functools import lru_cache (Python 2.7, 3.x)

+ Factor out temporary contexts

  - If you're repeating setup/teardown, use context managers
  - __enter__, __exit__, with statement
  - Release locks using try..finally (or puppies die every time)

    * Or ``with lock`` BOOM!

+ ``with irgnored(OSError)`` (Python 3.4)::

    from contextlib iport contextmanager
    @contextmanager
    def ignored(*exceptions):
        ## do a thing...

+ ``with redirect_stdout(f):`` (not even real yet!)

Expressive One-Liners
=====================

+ Don't put too much on one line; don't put too little either...
+ One logical line of code equals one sentence in English. 

  - No run-on sentences (statements) !

+ List comprehensions/generator expressions are more declarative.
+ Everywhere you use [] (list comp) try to use genexp instead
