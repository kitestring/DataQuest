/* 
Write a query that returns the 10 capital cities with the highest population 
ranked from biggest to smallest population.
You should include the following columns, in order:
	capital_city, the name of the city.
	country, the name of the country the city is from.
	population, the population of the city.
 */


SELECT c.name capital_city, f.name country, c.population FROM cities c 
INNER JOIN facts f ON f.id = c.facts_id
WHERE c.capital = 1
ORDER BY 3 DESC
LIMIT 10;


