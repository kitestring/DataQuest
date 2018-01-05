# Write a query that returns all of the years that the actress Natalie Portman was nominated for an award.
	# Only return the year column from ceremonies and the movie column from nominations.
	# Run the query and assign the full results list to the variable portman_movies.
	# Then display portman_movies using the print function.


import sqlite3

conn = sqlite3.connect('academy_awards.db')
cursor = conn.cursor()

q1 ='''SELECT * FROM movies_actors LIMIT 5;'''
five_join_table = conn.execute(q1).fetchall()
print('\nfive_join_table')
for fjt in five_join_table:
	print(fjt)
	
q2 ='''SELECT * FROM actors LIMIT 5;'''
five_actors = conn.execute(q2).fetchall()
print('\nfive_actors')
for fa in five_actors:
	print(fa)

q3 ='''SELECT * FROM movies LIMIT 5;'''
five_movies = conn.execute(q3).fetchall()
print('\nfive_movies')
for fm in five_movies:
	print(fm)

conn.close()

# output:

# five_join_table
# (1, 1, 1)
# (2, 2, 2)
# (3, 3, 3)
# (4, 4, 4)
# (5, 5, 5)

# five_actors
# (1, 'Javier Bardem')
# (2, 'Jeff Bridges')
# (3, 'Jesse Eisenberg')
# (4, 'Colin Firth')
# (5, 'James Franco')

# five_movies
# (1, 'Biutiful')
# (2, 'True Grit')
# (3, 'The Social Network')
# (4, "The King's Speech")
# (5, '127 Hours')