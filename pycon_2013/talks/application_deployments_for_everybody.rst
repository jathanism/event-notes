##################################################
Solid Python Application Deployments for Everybody
##################################################

:Date:
    2013-03-16

:Speaker:
    Hynek Schlawack

:Slides:
    http://ox.cx/d

Warnings
========

+ Heavy Opinions ahead
+ We're not talking about PaaS, schema migrations

Key Concepts
============

+ Responsible Deployment Cycle
+ Easy != Simple
+ "Simplicity is a prerequisite for realiablity." - Dijkstra

  - "... and security." - Every security expert ever

+ Put **effort** into making your deployments **simple**.

Development
===========

+ Always develop your app on the target platform
+ Avoid inevitable differences!
+ See: `Vagrant <http://vagrantup.com>`_ - Maci VM tool for devs.
+ What if?

  - Target platform: CentOS 5 (python 2.4.3 =( )
  - "Python 2.4 is not supported. It came out 8 years ago. Upgrade." - Kenneth
    Reitz

Stability
---------

+ You want a stable platform. Key infrastructure?
+ Use pre-built packages?
  
  - NO!
  - Unless you're writing a package FOR a distribution.
  - System packages are often spotty, usually outdated 

+ Use virtualenv!

  - Pin your deps hard: "Djang==1.4.3"
  - Don't rely on SemVer!!
  - Update w/ pip-tools

Security
--------

+ It's **your** job, no one else knows the app like you do.
+ You must be responsible for your own service.


Deployment Prequisites
======================

Package it!
-----------

+ Git + Fabric is "cool" but not stable.
+ Why?

  - Build tools on production services could be dangerous

    * resources
    * exploitation

  - Repetitive (compiling C extensions on every server? zzz)
  - Duplication

+ Use native packages (.rpm, .deb, .pkg)

  - You can tell "this server is on this version"
  - Introspection
  - CM integration
  - Versatility

+ You want reproducabliity. 

  - So you can scale.

+ Use FPM

 - You don't want to run your own repo server?
 - Use CLI tools (``rpm -i``, ``dpkg -i``)

Workflow
--------

1. check outfrom git
2. create virtualenv
3. install deps
4. do whatever you want
5. profit

+ Abuse the Pipeline?

  - Run tests
  - less/sass/cofeescript
  - compression
  - cache busting

Automate!
---------

+ Deployment (see his blog post)::

    from _ import Deployment
    def deb(branch=None):
        deploy = Deployment('whois', build_deps=['libp-dev'],
                            run_deps=['libpq5'])
        deploy.prepare_app(branch=branch)
        # ...

+ Parcel: 3rd party lib for x-platform packaging

Configuration
-------------

+ Don't put your configs in the package
+ Use config mgmt

  - Declarative, describe the goal
  - Let CM choose the path
  - Salt, Puppet, Chef, etc.

+ Not easy, make an informed choice.

Security
--------

+ Never use the same credentials between dev and prod.

  - You know, just in case.

+ Never run anything as root. Seriously, just don't.

  - Priveleged ports (<1024)? Drop privs after launch, use authbind.

+ Use single purpose wokrers (celery, rq)

  - e.g. "User creation worker", "Service restarting worker"
  - Isolate volatile tasks where logical

+ Be paranoid.

  + Use iptables to lock down *everything*
  + Use file sockets (file perms), no listening ports.

+ Each app should have its own user/group

  - Set shell to ``/bin/false``
  - Use fail2ban

+ Each app should have its own datbase and user


Test it in Staging
------------------

+ Staging must be an **exact** replica of production environment
+ Same platform, versions, etc.

Stability
---------

+ Don't run it in foreground using screen/tmux!
+ Daemonize everything

  - upstart (Ubuntu)
  - systemd
  - supervisord
  - circus

+ Apache + mod_wsgi is not your only choic!

  - mod_wsgi is overkill for most cases

+ (uWSGI or NGiNX) + gunicorn have better separation of duties

  - HTTP: uWSGI/nginx
  - WSGI: gunicorn
  - ssl, http -> https rediction, headers, etc.

Actually Deploying
==================

+ Given you've done everything above...
+ ... Once you get to this point, it should be easy.
+ It didn't work. Undo! Undo! Rollback! Oh no!!
  
  - Should also be as easy as reverting the package.

Metrics
-------

+ Predict problems before you have to solve them
+ Choices:

  - statsd
  - graphite
  - ganglia
  - scales
  - StatHat

+ MEASURE ALL THE THINGS

  - CPU, memory, requests in/out, db calls, login failures, etc.

Monitoring
----------

+ Pingdom, Nagios, etc.
+ Alerting/reporting

