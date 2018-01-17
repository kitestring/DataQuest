/* 
Write a query that returns the countries that don't exist in cities:
	Your query should return two columns:
		The country names, with the alias country.
		The country population.
	Use a LEFT JOIN to join cities to facts.
	Include only the countries from facts that don't have a corresponding value in cities.
 */


SELECT f.name country, f.population 
FROM facts f 
LEFT JOIN cities c ON c.facts_id = f.id
WHERE c.name IS NULL;


