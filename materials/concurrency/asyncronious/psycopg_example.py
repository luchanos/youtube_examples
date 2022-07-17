import psycopg2
from uuid import uuid4
from random import randint
from time import time, sleep

start = time()
conn = psycopg2.connect(dsn="postgresql://postgres:postgres@localhost:5432/postgres")
cursor = conn.cursor()
res = cursor.execute("SELECT * FROM users;")

with conn, cursor:
    for i in range(100_000):
        sleep(.1)
        cursor.execute("INSERT INTO users (username, rating) VALUES('%s', %d);" % (str(uuid4()), randint(0, 10000)))

print(time() - start)
