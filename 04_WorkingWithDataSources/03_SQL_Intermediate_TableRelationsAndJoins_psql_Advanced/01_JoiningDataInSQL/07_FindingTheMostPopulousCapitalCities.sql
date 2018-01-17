/* 
Write a query that returns the 10 capital cities with the highest population 
ranked from biggest to smallest population.
You should include the following columns, in order:
	capital_city, the name of the city.
	country, the name of the country the city is from.
	population, the population of the city.
 */


SELECT c.name capital_city, f.name country, c.population FROM facts f 
INNER JOIN (SELECT * FROM cities
			WHERE capital = 1 and 
			population > 10000000
			) c ON c.facts_id = f.id
ORDER BY 3 DESC
LIMIT 10;


