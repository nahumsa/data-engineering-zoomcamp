# Homework  <!-- omit in toc -->

# Table of contents  <!-- omit in toc -->
- [Ingesting data on postgres](#ingesting-data-on-postgres)
- [1 - Knowing docker tags](#1---knowing-docker-tags)
- [2 - Understanding docker first run](#2---understanding-docker-first-run)
- [3 - Count records](#3---count-records)
- [4 - Largest trip for each day](#4---largest-trip-for-each-day)
- [5 - The number of passengers (?)](#5---the-number-of-passengers-)
- [6 - Largest tip](#6---largest-tip)

------------------
# Ingesting data on postgres

You will need docker, docker-compose and Make.

1) Initiate the postgres database using `make start_db`;
2) Ingest the green trip data using `make ingestion_green_trip`;
3) Ingest the zones table using `make ingestion_zones`;
4) To tear down the project, you just need to run `make end_db`.


# 1 - Knowing docker tags

Run the command to get information on Docker

docker --help

Now run the command to get help on the "docker build" command

Which tag has the following text? - Write the image ID to the file

- [ ] --imageid string
- [x] --iidfile string
- [ ] --idimage string
- [ ] --idfile string

Solution:

```bash
docker build --help | grep "Write the image ID to the file"
```

# 2 - Understanding docker first run
Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list). How many python packages/modules are installed?

- [ ] 1
- [ ] 6
- [X] 3
- [ ] 7

Solution: The packages are:

```bash
Package    Version
---------- -------
pip        22.0.4
setuptools 58.1.0
wheel      0.38.4
```

# 3 - Count records
How many taxi trips were totally made on January 15?

Tip: started and finished on 2019-01-15.

Remember that lpep_pickup_datetime and lpep_dropoff_datetime columns are in the format timestamp (date and hour+min+sec) and not in date.

- [ ] 20689
- [X] 20530
- [ ] 17630
- [ ] 21090

Solution:

The query is in [`exercise_3.sql`](./exercise_3.sql). You can run in `pgcli` using `\i exercise_3.sql`.

# 4 - Largest trip for each day

Which was the day with the largest trip distance. Use the pick up time for your calculations.

- [ ] 2019-01-18
- [ ] 2019-01-28
- [X] 2019-01-15
- [ ] 2019-01-10

Solution:

The query is in [`exercise_4.sql`](./exercise_4.sql). You can run in `pgcli` using `\i exercise_4.sql`.

# 5 - The number of passengers (?)

In 2019-01-01 how many trips had 2 and 3 passengers?

- [ ] 2: 1282 ; 3: 266
- [ ] 2: 1532 ; 3: 126
- [X] 2: 1282 ; 3: 254
- [ ] 2: 1282 ; 3: 274

Solution:

The query is in [`exercise_5.sql`](./exercise_5.sql). You can run in `pgcli` using `\i exercise_5.sql`.

# 6 - Largest tip
For the passengers picked up in the Astoria Zone which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

Note: it's not a typo, it's tip , not trip

- [ ] Central Park
- [ ] Jamaica
- [ ] South Ozone Park
- [ ] Long Island City/Queens Plaza

Solution:

The query is in [`exercise_6.sql`](./exercise_6.sql). You can run in `pgcli` using `\i exercise_6.sql`.
