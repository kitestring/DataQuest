/* 
Write a query that uses multiple named subqueries in a WITH clause to gather total sales data on customers from India:
	The first named subquery should return all customers that are from India.
	The second named subquery should calculate the sum total for every customer.
	The main query should join the two named subqueries, resulting in the following final columns:
		customer_name - The first_name and last_name of the customer, separated by a space, eg Luke Skywalker.
		total_purchases - The total amount spent on purchases by that customer.
 */

WITH
    customers_india AS
        (
        SELECT * FROM customer
        WHERE country = 'India'
        ),
    sales_per_customer AS
        (
         SELECT
             customer_id,
             SUM(total) total
         FROM invoice
         GROUP BY 1
        )

SELECT
    ci.first_name || ' ' || ci.last_name customer_name,
    spc.total total_purchases
FROM customers_india ci
INNER JOIN sales_per_customer spc ON ci.customer_id = spc.customer_id