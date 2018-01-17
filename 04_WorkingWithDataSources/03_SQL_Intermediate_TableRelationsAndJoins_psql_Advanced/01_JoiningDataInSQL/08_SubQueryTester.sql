/* 
Write a query that generates output as shown above. The query should include:
	The following columns, in order:
		country, the name of the country.
		urban_pop, the sum of the population in major urban areas belonging to that country.
		total_pop, the total population of the country.
		urban_pct, the percentage of the population within urban areas, calculated by dividing urban_pop by total_pop.
	Only countries that have an urban_pct greater than 0.5.
	Rows should be sorted by urban_pct in ascending order.
 */


SELECT 
	SUM(population) urban_pop
FROM cities
GROUP BY Facts_id;