import sqlite3
conn = sqlite3.connect('factbook.db')

conn.execute("CREATE INDEX pop_pop_growth_idx ON facts(population, population_growth);")

query_plan_three = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.05;").fetchall()
print(query_plan_three)

# Output:
#     [(0, 0, 0, 'SEARCH TABLE facts USING INDEX pop_pop_growth_idx (population>?)')]