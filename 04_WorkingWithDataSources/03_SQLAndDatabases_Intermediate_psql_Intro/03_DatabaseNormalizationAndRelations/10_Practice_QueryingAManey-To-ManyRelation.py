# Write a query that returns all of the movies that "Natalie Portman" played in.
	# We want to return only the movie name (from the movies table) and the actor name (from the actors table).
	# You need to first join the movies table with the movies_actors table.
	# Then, you need to join the movies_actors table with the actors table.
	# Finally, you need to add a where statement that limits the results to just where actors.actor is equal to Natalie Portman.
# Run the query and assign the full results list to portman_joins.
# Use the print function to display portman_joins.

import sqlite3

conn = sqlite3.connect('academy_awards.db')

q1 = '''
SELECT movies.movie, actors.actor
FROM movies_actors
INNER JOIN actors
ON movies_actors.actor_id == actors.id
INNER JOIN movies
ON movies_actors.movie_id == movies.id
WHERE actors.actor == "Natalie Portman";
'''

portman_joins = conn.execute(q1).fetchall()
for pj in portman_joins:
	print(pj)