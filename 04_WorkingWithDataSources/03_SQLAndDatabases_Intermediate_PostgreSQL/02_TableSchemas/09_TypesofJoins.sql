/* 
INNER JOIN -- only displays rows where there is a match for the ON 
			condition in both tables. Any rows that aren't matched are excluded.
			
LEFT OUTER JOIN -- if there is no match for a row from the table on 
			the left side of the ON condition, it is shown with NULL 
			values for all the right side values.
			
RIGHT OUTER JOIN -- if there is no match for a row from the table 
					on the right side of the ON condition, it is shown 
					with NULL values for all the left side values.
 */
 
/*  
INNER JOIN is the most common type of join, but LEFT OUTER JOIN is also 
occassionally used. It's very uncommon to use RIGHT OUTER JOIN, and SQLite doesn't support it.
From a syntax points of view, using the statements is the exact same, you just swap out 
INNER JOIN for LEFT OUTER JOIN.
 */

/* 
Write a SQL query that:
	Uses the SELECT statement to query all the columns of the landmarks table.
	Uses LEFT OUTER JOIN to combine data from the landmarks table with data from the facts table.
	Uses the id column from facts and the country column of landmarks to perform the join.
 */
 
SELECT * FROM landmarks
LEFT OUTER JOIN facts 
ON landmarks.country = facts.id;