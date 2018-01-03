# Write and run a query that returns the Major and Major_category columns from recent_grads.
# Then, fetch the first five results and store them as five_results.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = 'SELECT Major, Major_category FROM recent_grads;'
cursor.execute(query)
five_results = cursor.fetchmany(5)