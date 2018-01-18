/* 
Use UNION to produce table of customers in the USA or have spent more than $90, 
using the customer_usa and customer_gt_90_dollars views:
	The result should contain the columns from customers, in their original order.
 */
 
SELECT * FROM customer_usa;

SELECT * FROM customer_gt_90_dollars;