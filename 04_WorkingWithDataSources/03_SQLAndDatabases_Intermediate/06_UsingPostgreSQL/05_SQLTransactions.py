import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
cur = conn.cursor()
cur.execute("Create Table notes (id INTEGER PRIMARY KEY, body TEXT, title TEXT)")
conn.commit()
cur.execute("select column_name from information_schema.columns where table_name = 'notes'")
conn.close()