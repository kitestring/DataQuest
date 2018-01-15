import sqlite3
conn = sqlite3.connect("factbook.db")
query_plan_one = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.05;").fetchall()
print(query_plan_one)


# Output:
#     [(0, 0, 0, 'SCAN TABLE facts')]