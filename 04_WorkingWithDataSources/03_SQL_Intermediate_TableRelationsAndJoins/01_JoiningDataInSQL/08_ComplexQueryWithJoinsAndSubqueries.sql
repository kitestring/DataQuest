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
	f.name country, 
	urban_pop,
	f.population total_pop,
	CAST(urban_pop as Float) / CAST(f.population as Float) urban_pct
FROM facts f 
INNER JOIN (
	SELECT 
		SUM(population) urban_pop,
		facts_id
	FROM cities
	GROUP BY Facts_id) c ON c.facts_id = f.id
WHERE
	urban_pct > 0.5
ORDER BY 4 ASC;


