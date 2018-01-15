/* 
Write a query that:
Joins cities to facts using an INNER JOIN.
Uses aliases for table names.
Includes, in order:
All columns from cities.
The name column from facts aliased to country_name.
Includes only the first 5 rows.
 */

SELECT c.*, f.name country_name FROM facts f 
INNER JOIN cities c ON f.id = c.facts_id
LIMIT 5;


