import sqlite3
conn = sqlite3.connect("factbook.db")

q4 = 'EXPLAIN QUERY PLAN SELECT * FROM facts WHERE id = 20;'
query_plan_four = conn.execute(q4).fetchall()

print('query plan 4')
print(query_plan_four)

# Output:
#     query plan 4
#     [(0, 0, 0, 'SEARCH TABLE facts USING INTEGER PRIMARY KEY (rowid=?)')]