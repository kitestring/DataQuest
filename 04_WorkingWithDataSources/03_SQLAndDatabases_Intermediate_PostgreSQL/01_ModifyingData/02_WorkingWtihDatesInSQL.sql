/* 
Select any rows from facts where 
updated_at is greater than October 30th, 2015 at 4pm, and 
updated_at is less than November 2nd, 2015 at 3pm.
 */
 
SELECT * FROM facts 
WHERE updated_at > "2015-10-30 16:00" AND
updated_at < "2015-11-02 15:00";