import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
cur = conn.cursor()
cur.execute("Create Table notes (id INTEGER PRIMARY KEY, body TEXT, title TEXT)")
conn.close()