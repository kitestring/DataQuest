import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
conn.autocommit = True
cur = conn.cursor()
cur.execute("Create Table facts (id INTEGER PRIMARY KEY, body TEXT, title TEXT)")
conn.close()