import psycopg2
import string
import random
import time
from config import host, user, password, db_name, port


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def execute_query(connect, query):
    with connect.cursor() as cursor:
        cursor.execute(query)
        print(f"[INFO] Execute query: {query}")


try:
    # connect to database
    connection = psycopg2.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=db_name,
                                  port=port)
    connection.autocommit = True

    create_table = """create table if not exists public.users(id serial PRIMARY KEY, \
name varchar(50) NOT NULL, \
nick_name varchar(50) NOT NULL, \
salary integer); \
alter table public.users replica identity full;"""
    # autocommit=True
    execute_query(connection, create_table)
    for _ in range(1000):
        name = generate_random_string(10)
        nick_name = generate_random_string(10)
        salary = int(random.uniform(0, 30000))
        insert_data = f"""insert into public.users(name, nick_name, salary) values \
('{name}', '{nick_name}', {salary})"""
        execute_query(connection, insert_data)

except Exception as e:
    print(f"ERROR: {e}")
finally:
    if connection:
        connection.close()
        print("Connection close")