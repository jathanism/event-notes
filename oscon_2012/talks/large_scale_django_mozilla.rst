=============================
Large Django sites at Mozilla
=============================

:Date:
    2012-07-19

:Speaker:
    Andy McKay

:Details:
    http://www.oscon.com/oscon2012/public/schedule/detail/24099

The Gist
========

+ Mozilla's addons site is a Django app
+ The upcoming App Store is too
+ `zamboni <https://mozilla.github.com/zamboni>`_ - Mozilla's Django app

How Big?
========

+ 300k+ addons
+ 150M unique views/month
+ 2B+ API hits/day
+ Backend:

  + MySQL
  + Memcache
  + Elasticsearch
  + Celery
  + RabbitMQ
  + Redis (being deprecated because clustering not in yet)

Monitoring
==========

+ Nagios (`zamboni-monitor <http://bit.ly/zamboni-monitor>`_)
+ Ganglia (hardware monitor)
+ Graphite (`django-statsd <http://bit.ly/django-statsd>`_)
+ Navigation timing API (http://w3.org/TR/navigation-timing)

Templating
==========


+ Jinja2 used for templating
+ jingo - template minification (css, js, etc.)

  + Adds build ids to file imports, too (e.g. ``foo.css?build_id=12345``)
    
Model Caching
=============

+ `cache-machine <http://bit.ly/cache-machine>`_

  + connections, models cached in memcache/redis
  + hashes query to map object to query
  + doesn't cache empty querysets

Search
======

+ Elasticsearch (https://github.com/mozilla/elasticutils)

Performance
===========

+ Async anything non-user-time
+ Be mindful of things that don't complete (use timeouts)
+ Process chunks asynchronously too using ``.values_list('pk')``::

    for chunk in chunks:
        task.delay(chunk)

+ `queryset-transform <http://bit.ly/queryset-transform>`_ - collapse chained
  queries
+ Firefox update URL gets ~8000 requests/sec

  + 1 hit per addon
  + addons are cached
  + 6400/sec cached; ~1600/sec raw

+ Legacy PHP app could handle 550 req/sec, stock Django only 150/sec
+ What if we use connection pooling (django-db-pool)?

  + Raw Django: 201/sec (wsgi was capped at 200/sec)
  + WSGI, no Django: 350/sec
  + Pooling, optimized queries: 700/sec (no Django, SQLAlchemy conn. pool)
    
Deployments
===========

+ Big Red Button that logs to IRC
+ django-waffle - flip features in your app
+ Email errors DO NOT SCALE (use Sentry)
