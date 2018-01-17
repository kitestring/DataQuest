import psycopg2
conn = psycopg2.connect(user="postgres")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE dq OWNER postgres;")
conn.close()