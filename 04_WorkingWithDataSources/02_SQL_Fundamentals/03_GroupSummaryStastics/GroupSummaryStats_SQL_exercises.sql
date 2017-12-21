/* 01_Introduction
	Write a SQL query that displays all of the columns and the first five rows of the recent_grads table. */
SELECT 
	* 
FROM
	recent_grads
LIMIT 5;
	
/* 02 Calculating Group-Level Summary Statistics
	Use the SELECT statement to select the following columns and aggregates in a query:
		Major_category
		AVG(ShareWomen)
	Use the GROUP BY statement to group the query by the Major_category column. */
SELECT 
	Major_category,
	AVG(ShareWomen)
FROM 
	recent_grads
GROUP BY 1;

/* 03 Practice: Using GROUP BY
	For each major category, find the percentage of graduates who are employed.
		Use the SELECT statement to select the following columns and aggregates in your query:
			Major_category
			AVG(Employed) / AVG(Total) as share_employed
		Use the GROUP BY statement to group the query by the Major_category column. */
SELECT 
	Major_category,
	AVG(Employed) / AVG(Total) as share_employed
FROM 
	recent_grads
GROUP BY Major_category;

/* 04 Querying Virtual Columns With the HAVING Statement
	Find all of the major categories where the share of graduates with low-wage jobs is greater than .1.
		Use the SELECT statement to select the following columns and aggregates in a query:
			Major_category
			AVG(Low_wage_jobs) / AVG(Total) as share_low_wage
		Use the GROUP BY statement to group the query by the Major_category column.
		Use the HAVING statement to restrict the selection to rows where share_low_wage is greater than .1. */
SELECT 
	Major_category,
	AVG(Low_wage_jobs) / AVG(Total) as share_low_wage
FROM 
	recent_grads
GROUP BY 1
HAVING
	share_low_wage > 0.1;
	
/* 05 Rounding Results With the ROUND() FUNCTION
	Write a SQL query that returns the following columns of recent_grads (in the same order):
		ShareWomen rounded to 4 decimal places
		Major_category
	Limit the results to 10 rows. */
SELECT 
	ROUND(ShareWomen, 4),
	Major_category
FROM
	recent_grads
LIMIT 10;

/* 06 Nesting Functions
	Use the SELECT statement to select the following columns and aggregates in a query:
		Major_category
		AVG(College_jobs) / AVG(Total) as share_degree_jobs
			Use the ROUND function to round share_degree_jobs to 3 decimal places.
	Group the query by the Major_category column.
	Only select rows where share_degree_jobs is less than .3. */
SELECT
	Major_category,
	ROUND(AVG(College_jobs) / AVG(Total), 3) as share_degree_jobs
FROM
	recent_grads
GROUP BY 1
HAVING
	share_degree_jobs < 0.3;
	
/* 07 Casting
	Write a query that divides the sum of the Women column by the sum of the Total column, aliased as SW.
	Group the results by Major_category and order by SW.
	The results should only contain the Major_category and SW columns, in that order. */
SELECT
	Major_category,
	SUM(CAST(Women as Float)) / SUM(CAST(Total as Float)) as SW
FROM
	recent_grads
GROUP BY 1
ORDER BY 2;