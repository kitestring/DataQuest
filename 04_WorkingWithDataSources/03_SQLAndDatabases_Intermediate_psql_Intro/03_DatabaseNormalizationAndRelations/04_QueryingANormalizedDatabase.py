# Write a query that returns all of the years that the actress Natalie Portman was nominated for an award.
	# Only return the year column from ceremonies and the movie column from nominations.
	# Run the query and assign the full results list to the variable portman_movies.
	# Then display portman_movies using the print function.


import sqlite3

conn = sqlite3.connect('academy_awards.db')
cursor = conn.cursor()

q ='''
SELECT 
	ceremonies.year, 
	nominations. movie 
FROM ceremonies
INNER JOIN nominations
ON ceremonies.id = nominations.ceremony_id
WHERE nominations.nominee = 'Natalie Portman';
'''

cursor.execute(q)
portman_movies = cursor.fetchall()
for p in portman_movies:
	print(p)
conn.close()