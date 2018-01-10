import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
cur = conn.cursor()
cur.execute("select column_name from information_schema.columns where table_name = 'notes'")
print(cur.fetchall())
conn.close()