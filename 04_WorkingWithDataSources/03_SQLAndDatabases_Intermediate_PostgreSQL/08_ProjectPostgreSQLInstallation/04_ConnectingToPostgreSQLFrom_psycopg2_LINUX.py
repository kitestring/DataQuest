import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres", host="/tmp/", password="Chlorine35%")
cursor = conn.cursor()
cursor.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
conn.close()