# Streaming data from Postres to MySql using Flink
Step by step launch of the pipeline
## 1) Creating a docker container with databases and Flink

```bash
docker compose up -d --build
```

## 2) Create table in POSTRES and start generate data
```bash
python3 /load_data/main.py
```

## 2) Create table in MySQL. Execute commands from Script.sql with #Create table mysql
```bash
python3 /load_data/main.py
```

## 3) Checking the id of the container
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

## 4) Entering the container with bash
```bash
docker exec -it <id_sql_client> /bin/bash
```

## 5) If necessary, we give the right to launch the sql-client
```bash
chmod u+x ./sql-client.sh
```

## 6) Start sql-client
```bash
./sql-client.sh
```

## 7) Execute commands from Script.sql with #FlinkSQL
```bash
set execution.checkpointing.interval=3s;
```
```bash
CREATE TABLE users (
    id INT, 
    name STRING, 
    nick_name STRING, 
    salary INT,
    PRIMARY KEY (id) NOT ENFORCED
) WITH (
   'connector' = 'postgres-cdc',
   'hostname' = 'localhost',
   'port' = '5432',
   'username' = '*****',
   'password' = '*****',
   'database-name' = 'db01',
   'schema-name' = 'public',
   'table-name' = 'users'
 );
```
```bash
CREATE TABLE usersnotsalary (
    id INT, 
    name STRING, 
    nick_name STRING,
    salary INT,
    PRIMARY KEY (id) NOT ENFORCED
) WITH (
   'connector' = 'jdbc',
   'url' = 'jdbc:mysql://localhost:3306/db02',
   'table-name' = 'users',
   'username'='*****',
   'password'='*****'
 );
```

```bash
INSERT INTO usersnotsalary
SELECT o.id, o.name, o.nick_name, o.salary + 1000
FROM users AS o;
```
## 8) Select in MySQL. Execute commands from Script.sql with #MySql. 
# Watch and enjoy
```bash
select * from users;
```
