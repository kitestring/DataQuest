/* 
Write a query that gathers data about the invoice with an invoice_id of 4. Include the following columns in order:
	The id of the track, track_id.
	The name of the track, track_name.
	The name of media type of the track, track_type.
	The price that the customer paid for the track, unit_price.
	The quantity of the track that was purchased, quantity.
 */
 
SELECT
	t.track_id,
	t.name track_name,
	mt.name track_type,
	il.unit_price,
	il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4;