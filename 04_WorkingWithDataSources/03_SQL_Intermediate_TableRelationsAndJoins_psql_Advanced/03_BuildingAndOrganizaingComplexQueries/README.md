### Procedure Change
The steps in this exercise are written for SQLite, and the *chinook.db* was provided.  To and an extra wrinkle the following alterations will be made to the steps to this exercise.

 *  Since this data set uses the same database as previous exercise *(02_IntermediateJoinsInSQL_psql-sqlite_convert)* I can continue utilizing the PostgreSQL managed database *chinook*.
 *  Recall a class was written to extract all the data from the SQL version of the DB and create each corresponding table and load the data into the PostgreSQL DB.
 *  Recall: to run a *.sql file from the PostgreSQL commandline use the folloiwing syntax: 
     *  psql -d chinook -U kitestring -w -f *.sql

 #### Database chinook Schema

 ![chinook-schema](https://s3.amazonaws.com/dq-content/189/chinook-schema.svg)
