import sqlite3
conn = sqlite3.connect('factbook.db')
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")

query_plan_five = conn.execute("EXPLAIN QUERY PLAN SELECT population FROM facts WHERE population > 1000000;").fetchall()
print(query_plan_five)

# Output:
#     [(0, 0, 0, 'SEARCH TABLE facts USING COVERING INDEX pop_idx (population>?)')]
