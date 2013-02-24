============================================
Automated Cloud Provisioning with Salt Cloud
============================================

:Speaker:
    Christer Edwards

:Date:
    2013-02-23

What is it?
===========

+ Disclaimer: THIS IS BETA!
+ Public cloud provisioning tool
+ Integrate into cloud providers cleanly, quickly, easily
+ Manage via maps and profiles
+ Pre-installs Salt, but doesn't have to be used
+ Meant to be a generic cloud mgmt thingy

Configuration
=============

+ Configs are yaml
+ Specify provider settings here, too.
+ Multiple providers works too

``/etc/salt/cloud``:: 

    minion:
        master: salt.domain.tld

Profiles
========

- Designate VMs inside profile config

``/etc/salt/cloud.profiles``::

    centos_linode:
        provider: linode
        image: CentoOS 6.2 64bit
        size: Linode 512
        minion:
            master.salt.domain.tld
        grains:
            role: webserver

+ Define Salt master and custom grains
+ Allows you to assing roles, or different masters per providers

  - See: Salt ``syndics``
  - Syndics are tiered masters (master -> sub-masters -> minions)
  - e.g. one syndic master per cloud provider
  - Controlled by master-master

Maps
====

+ Specify a prfile and then machines to make from it
+ Example::

    fedora_high:
        - redis1
        - redis2
        - redis3
    centos_high:
        - mysql1
        - mysql2
        - mysql3

Then run it::

    salt-cloud -m /path/to/map.file -P 
   
+ ``-P`` = parallel exec
+ Map files can also include grains!

Bootstrapping Salt
==================

+ Supports a few ways for strapping Salt onto new machines
+ ``script:`` (<0.8.4) config setting::
  
    fedora_linode:
        ...
        script: Fedora

+ ``salt-bootstrap`` (>=0.8.4) utility
+ src:``saltcloud/deploy`` has distro-specific insall scripts
  (e.g. ``Fedora.sh``)
+ >=0.8.4 if you omit ``script:``, ``salt-bootstrap`` is used
+ Update manually::

    salt-cloud [-u|--update-boostrap]

No Deployment
=============

+ You can provision without deploying Salt
+ ``deploy: False`` or ``script: None`` in profile
+ CLI: ``salt-cloud --no-deploy -p <profile> <instance>``

What's coming?
==============

+ Salt 0.14.0 will include ``salt-virt``
+ KVM support (libvirt)
+ ``salt.run virt.query``
+ ``salt.run virt.init $name $cpu $ram $image``
+ Serve images from ``salt://``, ``http://``, ``ftp://``
