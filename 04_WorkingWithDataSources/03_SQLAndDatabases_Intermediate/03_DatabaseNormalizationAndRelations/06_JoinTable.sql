CREATE table movies_actors (
id INTEGER PRIMARY KEY,
movie_id INTEGER REFERENCES movies(id),
actor_id INTEGER REFERENCES actors(id) 
);