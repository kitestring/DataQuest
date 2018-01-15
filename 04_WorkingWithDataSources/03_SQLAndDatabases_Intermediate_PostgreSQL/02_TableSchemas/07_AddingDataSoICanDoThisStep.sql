/* 
Write a SQL query that:
	Uses the SELECT statement to query all the columns of the landmarks table.
	Uses INNER JOIN to combine data from the landmarks table with data from the facts table.
	Uses the id column from facts and the country column of landmarks to perform the join.
 */
 
CREATE TABLE landmarks (
	id integer PRIMARY KEY,
	name text,
	country integer,
	FOREIGN KEY(country) REFERENCES facts(id)
);

INSERT INTO landmarks 
VALUES (1, "Statue of Liberty",186);

INSERT INTO landmarks 
VALUES (2, "Golden Gate Bridge",186);

INSERT INTO landmarks 
VALUES (3, "Washington Monument",186);

SELECT * FROM landmarks;