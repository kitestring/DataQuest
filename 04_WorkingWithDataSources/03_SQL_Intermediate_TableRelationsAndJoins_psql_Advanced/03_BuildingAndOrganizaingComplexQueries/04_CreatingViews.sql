/* 
Create a view called customer_gt_90_dollars:
	The view should contain the columns from customers, in their original order.
	The view should contain only customers who have purchased more than $90 in tracks from the store.
After the SQL query that creates the view, write a second query to display your newly created view: SELECT * FROM chinook.customer_gt_90_dollars;.
	Make sure you use a semicolon (;) to indicate the end of each query.
 */

CREATE VIEW customer_gt_90_dollars AS
 
	WITH total_puchased_info AS
		(
		SELECT 
			c.* 
		FROM invoice i
		INNER JOIN customer c ON c.customer_id = i.customer_id
		GROUP BY c.customer_id
		HAVING SUM(i.total) > 90
		)

	SELECT * FROM total_puchased_info;
