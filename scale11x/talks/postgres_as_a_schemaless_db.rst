===================================
PostgreSQL as a Schemaless Database
===================================

:Speaker:
    Chris Pettus

:Date:
    2013-02-22

:Site:
    thebuild.com

:Twitter:
    @xof

Basics
======

+ Requires PostgreSQL 9.2
+ NoSQL == Schemaless
+ Documents vs. rows
+ Persistent object storage

Types
=====

+ XML, JSON, hstore, relational

XML
---

+ Documents up to 2GB
+ Supports Xpath
+ No indexing :(

hstore
------

+ Heirarchial (docments link to documents)
+ Key/value store (strongs or other hstore objects/values)
+ GiST or GIN indexing on hstore values

JSON
----

+ Validates JSON going in
+ Indexable as text for strict comparison
+ Uses PL/V8
+ PL/V8 Pro-tips:

  - Use V8 that comes w/ PL/V8
  - Functions are not compiled by PL/V8 until first use
  - JSON injection is possible, stay vigilant
  - PL invocation is non-trivial (tangible overhead)

Comparison
==========

+ Side-by-side comparison of various types

  - Stock 9.2.2 install
  - Will compare against MongoDB
  - No tuning on app or system

Strategy
--------

+ Single-field tables w/ single type
+ Wrap queries in object-mapper
+ Index the column
+ Profit!

Performance
-----------

+ Test 1.78M records against MongoDB
+ Load/Disk/Query results ranked by fastest-to-slowest
+ For hstore, raw, GiST, and GIN are tested
+ For XML, JSON, MongoDB index type is expression index

==========  ======  =====  ======  ==========
Type        Index   Load   Disk    Query (pk)
==========  ======  =====  ======  ==========
relational  pk      1      6       2 
hstore      GiST    2,5,7  2,3,7   5,6,7
XML         expr    6      4       3
JSON        expr    3      5       1
MongoDB     expr    4      1       4
==========  ======  =====  ======  ==========

+ Query by name: hstore(GIN) is #1, JSON is #6
+ Query by pk: JSON is #1! (Thanks V8!)

Conclusions
===========

+ Stock MongoDB is doesn't seem to be more performant than PostgreSQL at
  querying documents when using accessor functions

  - Be realistic, test w/ real data

+ Index your accessor functions!
+ Avoid full-table scans
+ Consider hstore (most flexible)
+ GiST + GIN rock on high-entropy data (b-tree)

  - GIN outperforms GiST as dataset grows
