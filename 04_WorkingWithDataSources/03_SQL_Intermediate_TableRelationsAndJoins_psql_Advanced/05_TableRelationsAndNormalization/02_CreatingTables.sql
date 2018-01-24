/* 
Launch the SQLite shell and create a new database file, new_database.db.
Create a new table, user, with the following columns:
	user_id, with type INTEGER
	first_name, with type TEXT
	last_name, with type TEXT
Use the .schema dot command to view the schema for your newly created table.
Quit the SQLite shell.
 */
 
 Create DATABASE new_database;
 \c new_database;
 CREATE TABLE user_info (
				user_id INTEGER,
				first_name TEXT,
				last_name TEXT);
select column_name from information_schema.columns where table_name='user_info';