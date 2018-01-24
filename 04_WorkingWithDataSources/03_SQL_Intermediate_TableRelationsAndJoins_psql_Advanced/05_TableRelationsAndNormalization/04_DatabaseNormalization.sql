/* 
Launch the SQLite shell, connected to the chinook.db database.
Create a new table, wishlist_track:
	The table should have the following columns:
		wishlist_id, with type INTEGER.
		customer_id, with type INTEGER.
	A primary key should be specified, composed of both columns from the table.
	Each of the columns should be designated as a foreign key as indicated in the schema diagram.
Quit the SQLite shell.
 */
 
CREATE TABLE wishlist_track (
								wishlist_id INTEGER,
								track_id INTEGER,
								PRIMARY KEY (wishlist_id, track_id),
								FOREIGN KEY (wishlist_id) REFERENCES wishlist(wishlist_id),
								FOREIGN KEY (track_id) REFERENCES track(track_id));