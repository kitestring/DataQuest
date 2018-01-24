/* 
Launch the SQLite shell, connected to the chinook.db database.
Set all values for the active column in the wishlist table to 1.
Set all values for the active column in the wishlist_track table to 1.
Quit the SQLite shell.
 */
 
UPDATE wishlist SET active = 1;

UPDATE wishlist_track SET active = 1;