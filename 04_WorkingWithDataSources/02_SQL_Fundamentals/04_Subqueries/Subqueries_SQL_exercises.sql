/* 01 Writing More Complex Queries
	Try to write a query that answers the following question using the SQL you've learned so far:
		Which rows are above the average for the ShareWomen column? */
		
/* Note, this is not possible without using Subqueries */
SELECT 
	* 
FROM
	recent_grads
WHERE
	ShareWomen > AVG(ShareWomen);


/* 02 Subqueries
	Write a query that returns the majors that are below the average for Unemployment_rate. The results should:
		only contain the Major and Unemployment_rate columns
		be sorted in ascending order by Unemployment_rate */
SELECT Major, Unemployment_rate
FROM recent_grads
WHERE Unemployment_rate < (SELECT AVG(Unemployment_rate) FROM recent_grads)
ORDER BY 2 ASC;

/* 03 Subquery in SELECT
	Write a SQL statement that computes the proportion (as a float value) of rows that contain above average values for the ShareWomen.
	The results should only return the proportion, aliased as proportion_abv_avg, like so (with a different value): */
SELECT CAST(COUNT(*) as Float) / (SELECT CAST(COUNT(*) as Float) FROM recent_grads) as 'proportion_abv_avg'
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads);


/* 04 Returning Multiple Results in Subqueries
	Write a query that returns the Major and Major_category columns for the rows where:
		Major_category is one of the 5 highest group level sums for the Total column */
SELECT Major, Major_category
FROM recent_grads
WHERE Major_category IN (SELECT Major_category FROM recent_grads GROUP BY  Major_category ORDER BY SUM(Total) DESC LIMIT 5);

/* 05 Building Complex Subqueries
	Write a query that returns the average ratio (Sample_size/Total)) for all of the majors.
		You'll need to cast both columns to the float type.
		Use the alias avg_ratio for the average ratio. */
SELECT AVG(SampleRatio) as 'avg_ratio' FROM (SELECT CAST(Sample_size as Float)/CAST(Total as Float) as 'SampleRatio' FROM recent_grads);

/* 06 Practice Integrating A Subquery With the Outer Query
	Write a query that:
		selects the Major, Major_category, and the computed ratio columns
		filters to just the rows where ratio is greater than avgratio:
			recall that this value is the result of the subquery from the last screen: 
				select AVG(cast(Sample_size as float)/cast(Total as float)) avg_ratio from recent_grads */
SELECT 
	Major, 
	Major_category, 
	ratio
FROM (
	SELECT 
		Major, 
		Major_category, 
		CAST(Sample_size as Float)/CAST(Total as Float) as 'ratio' 
	FROM 
		recent_grads
	)
WHERE ratio > (SELECT 
					AVG(SampleRatio) as 'avg_ratio' 
				FROM (
					SELECT 
						CAST(Sample_size as Float)/CAST(Total as Float) as 'SampleRatio' 
					FROM recent_grads
					)
				);
				
