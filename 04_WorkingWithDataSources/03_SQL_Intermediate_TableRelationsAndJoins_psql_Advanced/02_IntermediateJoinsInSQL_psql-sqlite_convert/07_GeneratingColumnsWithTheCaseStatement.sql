/* 
Write a query that summarizes the purchases of each customer. For the purposes of this exercise, we do not have any two customers with the same name.

Your query should include the following columns, in order:
	customer_name - containing the first_name and last_name columns separated by a space, eg Luke Skywalker.
	number_of_purchases, counting the number of purchases made by each customer.
	total_spent - the sum of customers total purchases made by each customer.
	customer_category - a column that categorizes the customer based on their total purchases. The column should contain the following values:
	small spender - If the customer's total purchases are less than $40.
	big spender - If the customer's total purchases are greater than $100.
	regular - If the customer's total purchases are between $40 and $100 (inclusive).
	
Order your results by the customer_name column.
 */
 
SELECT
	c.first_name || ' ' || c.last_name employee_name,
	count(*) number_of_purchases,
	SUM(i.total) total_spent,
	CASE	
		WHEN SUM(i.total) < 40 THEN 'small spender'
		WHEN SUM(i.total) > 100 THEN 'big spender'
		ELSE 'regular'
		END
		AS customer_category
FROM invoice i
INNER JOIN customer c ON c.customer_id = i.customer_id
GROUP BY 1
ORDER BY 1 ASC;

/* 
Dataquest method, yet again they both work the same...
 */

SELECT
   c.first_name || ' ' || c.last_name customer_name,
   COUNT(i.invoice_id) number_of_purchases,
   SUM(i.total) total_spent,
   CASE
       WHEN sum(i.total) < 40 THEN 'small spender'
       WHEN sum(i.total) > 100 THEN 'big spender'
       ELSE 'regular'
       END
       AS customer_category
FROM invoice i
INNER JOIN customer c ON i.customer_id = c.customer_id
GROUP BY 1 ORDER BY 1;