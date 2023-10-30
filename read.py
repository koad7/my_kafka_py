#
# This file when ran will read data from postgres 
#
import psycopg2

conn = psycopg2.connect(
    "host=localhost dbname=dvdrental user=postgres password=manning"
)

cur = conn.cursor()

cur.execute("SELECT * from actor where first_name='change_to_actor' limit 5")

records = cur.fetchall()

print(records)