# Write a query that returns all of the values in the Major column from the recent_grads table.
# Store the full results set (a list of tuples) in majors.
# Then, print the first three tuples in majors.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "SELECT Major FROM recent_grads;"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:2])