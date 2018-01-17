/* 
Create a query that shows summary data about the playlists in the Chinook database:
	Use a WITH clause to create a named subquery with the following info:
		The unique ID for the playlist.
		The name of the playlist.
		The name of each track from the playlist.
		The length of the each track in seconds.
	Your final table should have the following columns, in order:
		playlist_id - the unique ID for the playlist.
		playlist_name - The name of the playlist.
		number_of_tracks - A count of the number of tracks in the playlist.
		length_seconds - The sum of the length of the playlist in seconds.
 */
 
WITH playlist_info AS
	(
	SELECT
		p.playlist_id playlist_id,
		p.name playlist_name,
		t.name track_name,
		(t.milliseconds / 1000) length_seconds
	FROM track t
	INNER JOIN playlist_track pt ON pt.track_id = t.track_id
	INNER JOIN playlist p ON p.playlist_id = pt.playlist_id
	)
	
SELECT
	playlist_id,
	playlist_name,
	COUNT(track_name) number_of_tracks,
	SUM(length_seconds) length_seconds
FROM playlist_info
GROUP BY 1,2;