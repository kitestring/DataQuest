/* 
Write a SQL query that:
	Uses the SELECT statement to query all the columns of the landmarks table.
	Uses INNER JOIN to combine data from the landmarks table with data from the facts table.
	Uses the id column from facts and the country column of landmarks to perform the join.
 */
 
SELECT * FROM landmarks
INNER JOIN facts 
on landmarks.country = facts.id;