/* 
Write a query that returns a information about each employer and their supervisor. 
Your query should return the following columns, in order:
	employee_name - containing the first_name and last_name columns separated by a space, eg Luke Skywalker
	employee_title - the title of that employee
	supervisor_name - the first and last name of the person the employee reports to, in the same format as employee_name
	supervisor_title - the title of the person the employee reports to
The report should include employees even if they do not report to another employee.
 */
 
SELECT
	e1.first_name || ' ' || e1.last_name employee_name,
	e1.title employee_title,
	e2.first_name || ' ' || e2.last_name supervisor_name,
	e2.title supervisor_title
FROM employee e1
LEFT JOIN employee e2 ON e1.reports_to = e2.employee_id;