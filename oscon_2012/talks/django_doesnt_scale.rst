=====================================================
Django Doesn't Scale! (And what you can do about it.)
=====================================================

:Date:
    2012-07-19

:Speaker:
    Jacob Kaplan-Moss

:Slides:
    https://speakerdeck.com/u/jacobian/p/django-doesnt-scale

The Gist
========

+ Large, successful services are using Django (Pinterest, Instagram)
+ "Django doesn't scale"
+ Frameworks don't scale!
+ Frameworks: Easy to start, then you hit a wall
+ See Cal Henderson's "Why I hate Django" on YouTube
+ "Measure twice, cut once."

Five Ways Django Fails
======================

1. Data collection
------------------

+ `Sentry <http://sentry.rtfd.org>`_
+ Python's ``logging`` module
+ python-statsd (used by Graphite)
+ mmstats (django-mmstats)
+ `Metrology <http://metrolog.rtfd.o>`_
+ `Graphite <http://graphite.rtfd.org>`_
+ New Relic - not free (Graham @ New Relic works on Python support)

2. Caching
----------

+ "Cache rules everything around me" (http://pyvideo.org/video/679)
+ "My pinstafacegramisqus is slow!"
+ Technique: Resource decomposition

  + edge-side includes (django-esi) ala Akamai, Varnish, et al.
  + 2-phase template rendering (django-phased)
  + client-side composition (e.g. using jQuery)
 
+ "There are only two hard problems in computer science: Cache invalidation,
  naming things, and off-by-one errors."

+ Technique: Serve everything from cache

  + regenerate cache in the background

3. Perceived Performance
------------------------

+ aka background tasks
+ A lie you should tell yourself: "Writes are 10x as expensive as reads."
+ Use celery to delay write operations

  + less efficient in aggregate, but...
  + better front-end performance

+ "Eventual consistency"

4. Metrics
----------

+ If you track one metric, track *query count*
+ View execution stops to wait for each query
 
  + Network latency -> db -> network latency
  + Queries happen synchronously
  + Every query blocks

+ Use these:

  + ``.select_related()``
  + ``.prefetch_related()``
  + raw queries

5. Database Optimization
------------------------

+ "ORM is the Vietnam of Computer Science" --Ted Neward
+ ORM Inefficiencies

  + Queryset cloning (chaining) is very heavy

    + Use the ``Q`` object (better)
    + Use raw queries

  + Model instantiation is *slow*

    + ~40k inits per second
    + Use ``.values()`` or ``.values_list()``

  + Saving models

    + Each row is updated in full (all columns)
    + Use ``.update()``

  + Bulk inserts are *slow*
 
+ Django needs to be db-agnostic, but *you* don't.

  + Push your db to the max
  + Don't rely on Django to optimize
