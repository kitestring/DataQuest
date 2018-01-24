/* 
Launch the SQLite shell, connected to the chinook.db database.
Create a new table, wishlist, with the following columns:
	wishlist_id, with type INTEGER.
		This column should be the primary key.
	customer_id, with type INTEGER.
		This column should have a foreign key relationship with the customer_id column from the customer table.
	name, with type TEXT.
Quit the SQLite shell.
 */
 
CREATE TABLE wishlist (
				wishlist_id INTEGER PRIMARY KEY,
				customer_id INTEGER,
				name TEXT,
				FOREIGN KEY(customer_id) REFERENCES customer(customer_id));