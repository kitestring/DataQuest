# Import the sqlite3 library into the environment.
# Then, use the sqlite3.connect() function to connect to jobs.db, and assign the Connection instance it returns to conn.

import sqlite3

conn = sqlite3.connect('jobs.db')
