# Close the connection to the database using the Connection instance method close().

import sqlite3
conn = sqlite3.connect("jobs.db")

conn.close()