/* 
Write a SQL query that creates a table called states in the factbook database that 
will contain information on each state in a country. It should have the following columns:
	id -- integer data type, should be a primary key.
	name -- text data type.
	area -- integer data type.
	country -- integer foreign key to the id column of the facts table.
 */
 

/* because of the way i run this code in the command line the db_name.table is not necessary,
just the new table name.  Below is that way that will work under different conditions like
in the dataquest example. */
 
/* CREATE TABLE factbook.states(
	id integer PRIMARY KEY,
	name text,
	area integer,
	FOREIGN KEY(country) REFERENCES facts(id)
); */

CREATE TABLE states(
	id integer PRIMARY KEY,
	name text,
	area integer,
	country integer,
	FOREIGN KEY(country) REFERENCES facts(id)
);
	
PRAGMA table_info(states);