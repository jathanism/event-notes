============================
Moving from Apps to Services
============================

:Date:
    2012-07-18

:Speaker:
    Craig Kerstiens

:Slides:
    https://speakerdeck.com/u/craigkerstiens/p/django-apps-to-services

The Gist
========

+ Build all your Django apps to expose a service
+ All inter-application chatter should be via services
+ Choose an API that works best for you (REST, SOAP, XMLRPC, etc.)

  + If you do, do it right: Follow best practices
  + Don't make up your own

MVC to API
==========

Application
-----------

:URLs:
    Controls entry points to views

:Views:
    Renders content using templates

:Models:
    Maps content to stored data

Service
-------

:Provider:
    Controls entry point to endpoints

:Endpoint:
    Renders content

:Contract:
    Maps to stored data

Compared
--------

=========== ========
Application Service       
=========== ========
URLs        Provider
Views       Endpoint
Models      Contract
=========== ========
