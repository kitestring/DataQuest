# Modify the query we wrote earlier to instead return all the actors that starred in The King's Speech.
	# We're interested in both the actor name as well as the movie name this time (in that order).
# Run the query and assign the results list to kings_actors.
# Then, use the print function to display kings_actors.

import sqlite3

conn = sqlite3.connect('academy_awards.db')

q1 = '''
SELECT actors.actor, movies.movie
FROM movies_actors
INNER JOIN actors
ON movies_actors.actor_id == actors.id
INNER JOIN movies
ON movies_actors.movie_id == movies.id
WHERE movies.movie == "The King's Speech";
'''

kings_actors = conn.execute(q1).fetchall()
for ka in kings_actors:
	print(ka)