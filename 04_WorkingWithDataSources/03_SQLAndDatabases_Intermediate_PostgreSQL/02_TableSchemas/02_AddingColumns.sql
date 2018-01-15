/* 
Write a SQL query that adds a column called leader to the facts table, with the data type text.
 */
 
ALTER TABLE facts
ADD leader text;

PRAGMA table_info(facts);