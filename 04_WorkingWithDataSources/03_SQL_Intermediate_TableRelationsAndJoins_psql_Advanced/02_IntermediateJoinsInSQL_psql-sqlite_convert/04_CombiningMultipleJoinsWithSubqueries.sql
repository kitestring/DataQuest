/* 
Write a query that returns the top 5 albums, as calculated by the number of times a track from that album has been purchased. 
Your query should return the following columns, in order:
	album, the title of the album
	artist, the artist who produced the album
	tracks_purchased the total number of tracks purchased from that album
Your query should list the albums from most tracks purchased to least tracks purchased.
 */
 
SELECT
	alb.title,
	art.name,
	sum(il.quantity) tracks_purchased
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN album alb ON alb.album_id = t.album_id
INNER JOIN artist art ON art.artist_id = alb.artist_id
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 5;

/* 
Dataquest had a different solution, but got the same query response.
 */
 
SELECT
    ta.album_title album,
    ta.artist_name artist,
    COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT
                t.track_id,
                al.title album_title,
                ar.name artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
GROUP BY 1, 2
ORDER BY 3 DESC LIMIT 5;