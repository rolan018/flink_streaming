## Streaming data from Postres to MySql using Flink
Step by step launch of the pipeline
# 1) Creating a docker container with databases and Flink

```bash
docker compose up -d --build
```
# 2) Checking the id of the container

```bash
docker ps
```
```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
22e3b95cd315   test_flink-sql-client   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   6123/tcp, 8081/tcp                                     sql-client
2a15d58f1104   flink:1.16.0            "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   6123/tcp, 8081/tcp                                     test_flink-taskmanager-1
b34debb3ef65   flink:1.16.0            "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   6123/tcp, 0.0.0.0:8081->8081/tcp, :::8081->8081/tcp    test_flink-jobmanager-1
a81d1ea85631   mysql:8.0               "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   test_flink-mysql-1
cc500855d225   debezium/postgres:13    "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp              test_flink-postgres_input-1
```
# 3) Entering the container with bash

```bash
docker exec -it <id_sql_client> /bin/bash
```
# 4) If necessary, we give the right to launch the sql-client
```bash
chmod u+x ./sql-client.sh
```
# 5) Start sql-client
```bash
./sql-client.sh
```
# 6) Execute commands in Scripts.sql with #FlinkSQL
