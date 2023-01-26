#Create table mysql
CREATE TABLE users (id INT not null auto_increment primary key, 
name varchar(50), 
nick_name varchar(50),
salary int);

#MySql

select * from users;
----------------------------------

#FLINKSQL

set execution.checkpointing.interval=3s;

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


INSERT INTO usersnotsalary
SELECT o.id, o.name, o.nick_name, o.salary + 1000
FROM users AS o;


