/* 
Launch the SQLite shell, connected to the chinook.db database.
Add new rows to the wishlist table, in order, as shown above.
Add new rows to the wishlist_track table, in order, as shown above.
Quit the SQLite shell.
 */
 
INSERT INTO wishlist VALUES
	(1,34,'Joao''s awesome wishlist'),
	(2,18,'Amy loves pop');
	
SELECT * FROM wishlist;

INSERT INTO wishlist_track VALUES
	(1, 1158),
	(1, 2646),
	(1, 1990),
	(2, 3272),
	(2, 3470);
	
SELECT * FROM wishlist_track;