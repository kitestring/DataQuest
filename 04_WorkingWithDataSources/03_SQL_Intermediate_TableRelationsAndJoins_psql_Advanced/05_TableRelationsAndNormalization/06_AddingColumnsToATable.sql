/* 
Launch the SQLite shell, connected to the chinook.db database.
Create a new column, active, in the wishlist table with type NUMERIC.
Create a new column, active, in the wishlist_track table with type NUMERIC.
Quit the SQLite shell.
 */
 
ALTER TABLE wishlist ADD COLUMN active NUMERIC;
ALTER TABLE wishlist_track ADD COLUMN active NUMERIC;
