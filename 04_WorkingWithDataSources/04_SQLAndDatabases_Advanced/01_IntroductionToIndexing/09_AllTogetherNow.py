import sqlite3
conn = sqlite3.connect("factbook.db")

q5 = 'EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000;'
query_plan_five = conn.execute(q5).fetchall()

print('query plan 5')
print(query_plan_five)

conn.execute("CREATE INDEX IF NOT EXISTS population_idx ON facts(population);")
print("\nCREATE INDEX IF NOT EXISTS population_idx ON facts(population);")

q7 = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000"
query_plan_seven = conn.execute(q7).fetchall()

print('\nquery plan 7')
print(query_plan_seven)

# Outputs:
#     query plan 5
#     [(0, 0, 0, 'SCAN TABLE facts')]
#     
#     CREATE INDEX IF NOT EXISTS population_idx ON facts(population);
#     
#     query plan 7
#     [(0, 0, 0, 'SEARCH TABLE facts USING INDEX population_idx (population>?)')]
