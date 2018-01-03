# Now let's practice the entire workflow we've learned so far, from start to finish.
    # Connect to the database jobs2.db, which contains the same data as jobs.db.
    # Write and execute a query that returns all of the majors (Major) in reverse alphabetical order (Z to A).
    # Assign the full result set to reverse_alphabetical.
    # Finally, close the connection to the database.

import sqlite3
conn = sqlite3.connect('jobs2.db')
cursor = conn.cursor()

query ='SELECT Major FROM recent_grads ORDER BY 1 DESC;'
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
conn.close()