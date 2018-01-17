/* 
You have just returned from lunch to see another phone message on your desk: "Call Belle". 
Write a query that finds the contact details a customer with a first_name 
containing Belle from the databasc.

Your query should include the following columns, in order:
	first_name
	last_name
	phone
 */
 
SELECT
	c.first_name,
	c.last_name,
	c.phone
FROM customer c
WHERE LOWER(c.first_name) LIKE '%belle%';