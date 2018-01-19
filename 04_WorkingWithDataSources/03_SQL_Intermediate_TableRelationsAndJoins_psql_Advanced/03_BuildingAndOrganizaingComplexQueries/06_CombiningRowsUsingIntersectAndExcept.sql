/* 
Write a query that works out how many customers that are in the USA and have purchased more than $90 are assigned to each sales support agent. For the purposes of this exercise, no two employees have the same name.
Your result should have the following columns, in order:
	employee_name - The first_name and last_name of the employee separated by a space, eg Luke Skywalker.
	customers_usa_gt_90 - The number of customer assigned to that employee that are both from the USA and have have purchased more than $90 worth of tracks.
The result should include all employees with the title "Sales Support Agent", but not employees with any other title.
Order your results by the employee_name column.
 */
 
WITH customers_usa_gt_90 AS
    (
     SELECT * FROM customer_usa

     INTERSECT

     SELECT * FROM customer_gt_90_dollars
    )

SELECT
    e.first_name || ' ' || e.last_name employee_name,
    COUNT(c.customer_id) customers_usa_gt_90
FROM employee e
LEFT JOIN customers_usa_gt_90 c ON c.support_rep_id = e.employee_id
WHERE e.title = 'Sales Support Agent'
GROUP BY 1 ORDER BY 1;