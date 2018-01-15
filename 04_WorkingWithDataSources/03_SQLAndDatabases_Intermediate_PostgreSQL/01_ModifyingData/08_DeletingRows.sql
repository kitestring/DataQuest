/* 
Write a SQL query that removes all the rows in facts where name equals Canada.
*/

SELECT 'Before Canada Deletion';

SELECT * FROM facts
WHERE name = 'Canada';

DELETE FROM facts
WHERE name = 'Canada';

SELECT 'AFTER Canada Deletion';
 
SELECT * FROM facts
WHERE name = 'Canada';