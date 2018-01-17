/* 
Write a query that returns all columns from the facts and cities tables.
	Use an INNER JOIN to join the cities table to the facts table.
	Join the tables on the values where facts.id and cities.facts_id are equal.
	Limit the query to the first 10 rows.
 */

SELECT * FROM facts
INNER JOIN cities ON
facts.id = cities.facts_id
LIMIT 10;


