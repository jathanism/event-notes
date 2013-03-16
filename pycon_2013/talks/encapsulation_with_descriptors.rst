##############################
Encapsulation with Descriptors
##############################

:Date:
    2013-03-15

:Speaker:
    Luciano Ramalho
    
Assumptions
===========

+ You know the basics of classes/objects
+ New- vs old-style classes

The Scenario
============

+ Selling organic bulk foods
+ An order has several items
+ Each item has desc, weight, prices, subtotal (weight * price)

A Simple object
---------------

+ Too simple? What about a negative weight?
+ Amazon found customers could order negative quantity and it would credit
  their cards!!

Classic Solution
================

+ Getters/setters

  - Breaks existing code
  - Protected attributes are no fun
  
+ Protected attributes in Pyhton exist for safety

  - to avoid accidental assignment/override
  - to prevent intentional use/misuse

Validation with property
========================

+ Implement ``weight`` as a property::

    @property
    def weightself):
        return self.__weight

    @weight.setter:
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

+ What if we want to do the same thing to ``price``?
+ Duplicate the getter/setter but for ``price``?

Descriptors!
============

+ Abstraction of getters/setters
+ Manage access to weight/price attrs::

    class Quantity(object):
        __counter = 0

        def __init__(self):
            prefix = '_' + self.__class__.__name__
            key = self.__class__.__counter
            self.target_name = '%s_%s' % (prefix, key)
            self.__class__.__counter += 1

        def __get__(self, instance, owner):
            return getattr(instance, self.target_name)

        def __set__(self, instance, value):
            if value > 0:
                setattr(instance, self.target_name, value)
            else:
                raise ValueError('value must be > 0')

    class LineItem(object):
        weight = Quantity()
        price = Quantity()

+ Get/set logic moved to ``Quantity`` descriptor class.
+ These instances are created at import time
+ Each access goes thru their descriptor

What is a descriptor?
=====================

+ A descriptor is any class that defines ``__get__``, ``__set__``, or
  ``__delete__``
+ ``target_name`` is the name of the attribute from the caller (aka instance)
+ Each ``Quantity`` instance must create and use a unique a target attribute name
+ e.g. ``LineItem._Quantity_0``, ``LineItem._Quantity_1``

  - Instead of using a counter, perhaps you can use ``id()`` of the object

Room for improvement
====================

+ What about making them more descriptive: ``LineItem__weight``.
+ The challenge

  - When descriptor instantiated, LineItem class does not exist and attributes
    don't exist either.

What now?
=========

+ If descirptor needs to know the name of the managed class attr...
+ ... Then you need to control construction using a METACLASS!
+ COMPLEXITY!

References
==========

+ Raymond Hettinger's "Descriptor HowTo Guide"
+ Alex Martelli's "Python in a Nutshell 2e"
+ Dave Beazley "Python Essential Reference 4e"

By the Way
==========

+ All Python functions are descriptors

  - They implement ``__get__``

+ That's how a function becomes bound to an instance 

  - ``fn.__get__`` returns a partial
  -  this fixes the first arg (``self``) to the target instance
