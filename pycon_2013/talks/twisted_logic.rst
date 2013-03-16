#############
Twisted Logic
#############

:Date:
    2013-03-15

:Speaker:
    Ashwini Oruganti
    
What it is?
===========

+ Async event-driven networking framework
+ aka... HARD

Endpoints
=========

+ Interface w/ a single method that takes an argument
+ Use-case, make v4 server work w/ v6.
+ Next-case: stdio endpoint.
+ You don't have to write your own endpoints. Write interfaces instead.

Don't be afeared
================

+ It's just code.
+ Or something...

Deferreds
=========

+ Callbacks vs. errbacks
+ Flow is not obvious
+ Debugging is tricky
+ Firing a Deferred is like putting an item into a list with one method, and
  then returning the value from another

Twisted is HARD
===============
`
+ It's 'X', when it isn't really 'X'.
+ It's full of highly complex objects
+ The problem is how we typically view programs

  - It's like Russian stacking dolls.
  - Async code doesn't work that way.

+ camelCase (PEP-8: 2001-07-05, Twisted: 2001-05-02)
+ It's huge!!
