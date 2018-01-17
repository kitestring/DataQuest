import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
cur = conn.cursor()
print(cur)
conn.close()