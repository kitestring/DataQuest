/* 
Write a SQL query that uses the UPDATE statement to update any rows 
where name is United States to DataquestLand.
*/

SELECT * FROM facts
WHERE name = 'United States';

SELECT '';

UPDATE facts
SET name = 'DataquestLand'
WHERE name = 'United States';
 
SELECT * FROM facts
WHERE name = 'DataquestLand';