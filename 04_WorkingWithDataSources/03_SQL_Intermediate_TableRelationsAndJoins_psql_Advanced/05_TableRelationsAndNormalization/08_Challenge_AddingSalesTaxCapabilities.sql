/* 
Launch the SQLite shell, connected to the chinook.db database.
Add two new columns, with values, to the invoice table:
	tax, with type NUMERIC.
		The value for all existing rows should be 0.
	subtotal, with type NUMERIC.
		The value for each row should be the same as that row's value for total.
Quit the SQLite shell.
 */

ALTER TABLE invoice ADD COLUMN tax NUMERIC; 
ALTER TABLE invoice ADD COLUMN subtotal NUMERIC;

UPDATE invoice SET tax = 0;
UPDATE invoice SET subtotal = invoice.total;