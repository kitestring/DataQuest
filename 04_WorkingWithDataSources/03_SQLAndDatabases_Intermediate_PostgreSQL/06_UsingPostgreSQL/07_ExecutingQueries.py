import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute("SELECT * FROM notes;")
rows = cur.fetchall()
print(rows)
conn.close()