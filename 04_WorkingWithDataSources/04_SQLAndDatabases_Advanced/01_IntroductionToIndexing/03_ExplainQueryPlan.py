import sqlite3
conn = sqlite3.connect("factbook.db")

q1 = 'EXPLAIN QUERY PLAN SELECT * FROM facts WHERE area > 40000;'
query_plan_one = conn.execute(q1).fetchall()

q2 = 'EXPLAIN QUERY PLAN SELECT area FROM facts WHERE area > 40000;'
query_plan_two = conn.execute(q2).fetchall()

q3 = "EXPLAIN QUERY PLAN SELECT * FROM facts WHERE name = 'Czech Republic';"
query_plan_three = conn.execute(q3).fetchall()

print('query plan 1')
print(query_plan_one)

print('\nquery plan 2')
print(query_plan_two)

print('\nquery plan 3')
print(query_plan_three)

# Outputs:
#     query plan 1
#     [(0, 0, 0, 'SCAN TABLE facts')]
#     
#     query plan 2
#     [(0, 0, 0, 'SCAN TABLE facts')]
#     
#     query plan 3
#     [(0, 0, 0, 'SCAN TABLE facts')]
