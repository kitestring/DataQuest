/* 
Write a SQL query that returns the data type of each column in facts.
 */
 
PRAGMA table_info(facts);

/* 
This will output a the following columns:
	cid: Column ID
	name: Column name
	type: Column Data Type
	notnull: The value cannot be null (1 = true, 0 = false)
	dflt_value: default value ?
	pk: primary key (1 = true, 0 = false)
*/