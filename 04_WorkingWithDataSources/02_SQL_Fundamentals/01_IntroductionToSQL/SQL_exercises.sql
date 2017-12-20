/* 
02_Previewing A Table using SELECT
	Write a SQL query that returns the first 10 rows from recent_grads.
 */
SELECT * FROM recent_grads LIMIT 10;

/* 
03_Filtering Rows Using WHERE
	Write a SQL query that returns the majors where females were a minority.
	Only return the Major and ShareWomen columns (in that order) and don't limit the number of rows returned.
 */
SELECT MAJOR, ShareWomen  FROM recent_grads
WHERE ShareWomen < 0.5;

/* 
04_Expressing Multiple Filter Criteria Using AND
	Write a SQL query that returns:
		all majors with majority female and
		all majors had a median salary greater than 50000.
	Only include the following columns in the results and in this order:
		Major
		Major_category
		Median
		ShareWomen
 */
SELECT 
	Major, Major_category, Median, ShareWomen 
FROM 
	recent_grads
WHERE
	ShareWomen > 0.5 AND
	Median > 50000;
	

/* 05_Reurning One Of Several Conditions with OR
	Write a SQL query that returns the first 20 majors that either:
		have a Median salary greater than or equal to 10,000, or
		have less than or equal to 1,000 Unemployed people
	Only include the following columns in the results and in this order:
		Major
		Median
		Unemployed
 */
SELECT 
	Major, Median, Unemployed 
FROM 
	recent_grads
WHERE
	Median >= 10000 OR
	Unemployed <= 1000
LIMIT
	20;
	
/* 06_Grouping Operators with Parentheses
	Run the query we explored above, which returns all Engineering majors that:
		either had mostly women graduates
		or had an unemployment rate below 5.1%, which was the rate in August 2015
	Only include the following columns in the results and in this order:
		Major
		Major_category
		ShareWomen
		Unemployment_rate */
SELECT 
	Major, Major_category, ShareWomen, Unemployment_rate
FROM 
	recent_grads
WHERE 
	(Major_category = 'Engineering') AND 
	(ShareWomen > 0.5 OR 
	Unemployment_rate < 0.051);

/* 07_Ordering Results Using ORDER BY
	Write a query that returns all majors where:
		ShareWomen is greater than 0.3
		and Unemployment_rate is less than .1
	Only include the following columns in the results and in this order:
		Major,
		ShareWomen,
		Unemployment_rate
	Order the results in descending order by the ShareWomen column. */
SELECT 
	Major, ShareWomen, Unemployment_rate
FROM
	recent_grads
WHERE
	ShareWomen > 0.3 AND
	Unemployment_rate < 0.1
ORDER BY 2 DESC;

/* 08_Practice Writing a Query
	Write a query that returns the Engineering or Physical Sciences majors in asecending order of unemployment rates.
		The results should only contain the Major_category, Major, and Unemployment_rate columns. */
SELECT
	Major_category, Major, Unemployment_rate 
FROM
	recent_grads
WHERE
	Major_category = 'Engineering' or
	Major_category = 'Physical Sciences'
ORDER BY 3 ASC;
	