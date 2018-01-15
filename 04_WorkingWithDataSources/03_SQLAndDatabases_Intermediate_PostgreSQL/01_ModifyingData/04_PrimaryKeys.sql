/* 
Write a SQL query that uses the ORDER BY and LIMIT statements 
to select the entire row that has the highest id value.
*/

SELECT * FROM facts
ORDER BY id DESC
LIMIT 1;

/* 
Output:
261|xx|World||||7256490011|1.08|18.6|7.8||2015-11-01 13:39:09.910721|2015-11-01 13:39:09.910721
*/