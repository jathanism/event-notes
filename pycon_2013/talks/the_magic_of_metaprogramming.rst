############################
The Magic of Metaprogramming
############################

:Date:
    2013-03-15

:Speaker:
    Jeff Rush

What it is?
===========

+ Code that writes, analyzes, or adjusts other code
+ Makes uses of metaclasses, decorators, descriptors
+ Python 2.x, new-style classes

Model
=====

+ Code -> Data ->  Events
+ Metaprogramming injects Metacode 

  - adding attributes
  - adjusting values
  - registering instances
  - tagging objects
  - latching onto events

Example
=======

+ Subclass Request object without modifying the original code
+ Catch the import!
+ Redfine class to be subclass
+ Hook to after import 
+ Inspect which module is being imported
+ Re-arrange module
+ Return the module
+ ``from tau.metaservices import MetaServices``


You can subclass a module!!
===========================

+ stdlib: ``ihooks`` module

  - ``ihooks.ModuleImporter``
  - ``ihooks.FancyModuleLoader``

+ ``import types; types.ModuleType``
+ ``class MyModule(types.ModuleType): ...``

How we got here
===============

+ Variables, functions, code, blah...
+ Rise of C structs, grouping variables into namespaces
+ Promotion of functions to "variables"
+ Namespace "assembly function" aka constructors
+ Prototype pattern: stamp out copies (or instances of objects)
+ Shared vs. non-shared namespaces (module vs. instance)
+ Rise of iterative lookup (aka scoping)
+ Stuff that things have in common (aka classes)
+ Classes of classes (aka inheritance)
+ Parent classses (aka multiple inheritance)
+ Who is creating the classes (aka metaclasses)
+ Subclass your metaclasses!

Metaclasses
===========

+ Metaclass is a "kind of class"
+ New kinds useful for:

  - wrapping complexity
  - domain specific stuff
  - generate classes dynamically (e.g. XML DTDs)

+ Example: Create class object from database table
