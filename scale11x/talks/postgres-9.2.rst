======================================
Full Throttle Database: PostgreSQL 9.2
======================================

:Speaker:
    Josh Berkus

:Date:
    2013-02-22
    
New Features
============

+ Latest: 9.2.2
+ Read Scalability (350,000+ QPS?!)
+ Write Performance
+ Parallel Bulk Load - FASTEST POSTGRES EVER

  - 10-15 paralell streams (depending on CPU)
  - ~3x load speed

+ Index-Only Scans

  - Problem: "count(*)" is slow in PG
  - Looks at "Visibility Map", skip table lookup
  - Default: sequential scan, index-only: ~50% faster FOR FREE

+ Cascading Replication

  - Traditional replication puts heavy load on master's network interface 
  - You may now replicate from a replica ("replica master")
  - p2p replication!
  - It's easy:

    * % pg_basebackup -h replica-master -P -x -D .
    * primary_conninfo=
    * from replica-master: "select client_addr from pg_stat_replication;"
    * from master-master: "select client_addr from pg_stat_replication;"

+ Replication Improvements

  - recv vs. write modes for synchronous replication
  - satandby-only backup

+ JSON

  - JSON data type: STORE JSON TOO!!
  - Array_to_json, row_to_json functions
  - Get query results as JSON!
  - "select row_to_json(books.*) from books;"
  - Cut out the middle-man transcoding between JSON!

+ PL/v8 - Pluggable JavaScript engine

  - Create PL plugins using... JS
  - Create indexes based on JS functions!
  - "create index bibrec_author on json_val('author')..."
  - PL/coffee!

+ Indexing

  - 7.1: GiST - Generalized Search Tree (ranges, boxes)
  - 8.1: GIN - Generalized Inverted Index (default for full-text search, arrays)
  - 9.1: KNN - K-Neartest Neighbor (promixity, GIS, text similarity/trigrams)
  - 9.2: Space-GiST!

    * "Space-Partitioning Trees"
    * Faster to read/update than GiST!
    * "create index pt_gist_idx on geo using gist(point);"
    * "create index pt_gist_idx on geo using spgist(point);"

+ Range Types

  - Temporal range: [2012-04-10, 2012-04-12]

    * Types: tstzrange, timestamptz
    * "select * from copy_hostory where period @> timestamptz '2010-05-01';"

  - Alpha index: [Abbe, Babel]
  - Linear distance: [375.453, 374.441]

+ DDL pit stop

  - ALTER IF EXISTS
  - DROP INDEX CONCURRENTLY
  - NOT VALID CHECK constraints

+ Instrumentation

  - Get good knowledge of what your db is doing and how it do
  - more autovacuum logging
  - "pg_stat_statements" extension (must be installed) - Real-time stats
  - "select * from pg_stat_statements order by total_time desc;"

    * Not as rich as parsing query logs, but instantly available!

+ Better EXPLAIN

  - report filtered-out rows
  - no-TIMING option
  - "explain (analyze on, buffers on) select * from pegbench_accounts;"

+ Other
  - lower CPU wakeups (power saving)
  - pg_hba.conf improvements (readability mostly)
  - XML "improvements"
