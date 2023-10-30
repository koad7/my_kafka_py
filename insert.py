#
# This file when ran will read insert data into postgres
#
import psycopg2

conn = psycopg2.connect(
    "host=localhost dbname=dvdrental user=postgres password=manning"
)

cur = conn.cursor()

cur.execute("""
INSERT INTO ACTOR (first_name, last_name) 
VALUES(%s,%s)""", ("manning", "publications"))

conn.commit()
cur.close()
conn.close()