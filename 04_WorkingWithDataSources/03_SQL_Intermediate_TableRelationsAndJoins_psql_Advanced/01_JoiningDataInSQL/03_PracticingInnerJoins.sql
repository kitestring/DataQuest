/* 
Write a query that returns, in order:
	A column of country names, called country.
	A column of each country's capital city, called capital_city.
Use an INNER JOIN to join the two tables in your query.
 */


SELECT f.name country, c.name capital_city FROM cities c 
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1;


