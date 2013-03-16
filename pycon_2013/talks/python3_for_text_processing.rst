###############################################
Why You Should Use Python 3 for Text Processing
###############################################

:Date:
    2013-03-16

:Speaker:
    David Mertz

Why?
====

+ Native unicode (str is unicode, bytes is str)
+ String and bytes have grown handy methods
+ Wrote "Text Processing in Python" (download: http://gnosis.cx/TPiP)
+ Impressionistic review of nice-to-have improvements
+ These features are backported into 2.7

  - 3.1 -> 2.7
  - 3.2 -> 2.7.3
  - 3.3 -> 2.7.4?

Cool Stuff in collections
=========================

+ namedtuple, OrderedDict, HashMap

namedtuple
----------

+ Useful for dealing with CSV and database rows::

    import csv, collections
    users = open('user'csv')
    headers = users.readline()
    UserRecord = collections.namedtuple('UserRecord', headers)
    for row in csv.reader(users, rename=True):
        print(UserRecord(*row))
  
+ If you set ``rename=True`` it renames attributes that may be reserved types
+ Less memory than dicts (because of __slots__)

Counters
--------

+ Useful for histograms (such as commonality of letters)::

    import collections
    c1 = collections.Counter('abracadabra')
    print c1.most_common(4)
    # 3.3 only:
    # c1['d'] -= 10

+ Pseudo-arithmetic stuff, basically defaultdict to value 0::
  
    c2 = Counter('ramalama bim boom')
    (c1 + c2).most_common(4)
    # +c1 Increment

ChainMap
--------

+ New in Python 3.3
+ Collection of mappings... "container of containers"
+ Sneaky equiv. to dnyamic inheritance and MRO
+ ChainMaps can include ChainMaps::

    d1 = {'a':, 1, 'b': 2}
    d2 = {'c':, 3, 'd': 4}
    chian = ChainMap(d1, d1)
    print chain['a'], chain['d]
    # => (1, 4)

Unicode is hard
===============

+ *Most* (not all!) Unicode is in the BMP (Basic Multilingual Plane)
+ All of Latin-1 is in range 00 of the BMP
+ Internal encoding matters

  - Fixed-width (UTF-32/UCS-4): Uses a lot of memory
  - Variable-width (UTF-8): positing indexing is very slow
  - With UTF-16/UCS-2 you get the worst of everything:

    * Not strictly fixed-width (i.e. surrogate pairs)
    * Usually wasted memory

+ I have no idea what any of this means (fixed- vs. variable- width)

PEP-393
=======

+ Strings are normally Latin-1
+ Python encodes everything in the most compact form it can.
+ v3.3 adds back explicit unicode literals ``u'bacon'``.

Pro Tips
========

+ ``str.startswith()`` and ``str.endswith()`` take tuples as well a string 

  - (But not lists or other iterables)

+ Module ``textwrap``

  - People reimplment this over-and-over (*cough* Trigger)
  - Don't roll your own::

      textwrap.fill(s, width=35, initial_indent='| ', subsequent_indent='| '))

  - Dedent multiline strings::

      multiline = """
      foo
      bar
      bacon"""
      multi_line = textwrap.dedent(multi_line)

  - ``textwrap.indent()`` new in Python 3.3::

      def my_pred(line):
        return not line.endswith('wrote:\n')
      print(textwrap.indent(s, '| ', predicate=my_pred))
    
+ Module html.entities::

    from html.entities import h5ml5, entitydefs, codepoint2name
    print html5['Exists;']

+ Module unicodedata

  - Get names of glyphs
  - Validate, inspect

+ Proper quoting

  - Hidden in ``pipes.quote()``
  - In Python 3.3 it's moved to ``shlex.quote()``
  - Useful for generating shell scripts or CLI/subprocess args

+ Use ``format()``

  - Mini language
  - More powerful and robust than '%s' style.
  - e.g. Thousand separator (locale aware)

    * ``'${:,.2f}'.format(1000000) # => '$1,000,000.00'``
    * This is in Python 2.7, also

+ Module email

  - ``msg = email.message_from_file(...)``
  - ``payload = msg.get_payload()``
  - ``payload.get_content_type()``
