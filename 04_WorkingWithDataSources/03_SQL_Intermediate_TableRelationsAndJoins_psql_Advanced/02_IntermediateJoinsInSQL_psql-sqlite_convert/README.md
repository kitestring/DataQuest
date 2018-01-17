### Procedure Change
The steps in this exercise are written for SQLite, and the chinook.db was provided.  To and an extra wrinkle the following alterations will be made to the steps to this exercise.

 1.  Using the PostgreSQL command line the user ken_kite should be added with permission to create databases.  The syntax for this will be saved on *"PostgreSQLCommandLine_Setup.txt"*.
 1.  A new module will be written with a class to extract the data from the chinook.db and load it into a PostgreSQL managed database.
 1.  Then the remainder of the steps will be done using PostgreSQL rather than SQLite.		  1.  Then the remainder of the steps will be done usisng PostgreSQL rather than SQLite.
 1.  Using the PostgreSQL command line the user ken_kite should be added with permission to create databases.  The syntax for this will be saved on *"PostgreSQLCommandLine_Setup.txt"*.
 1.  Furthermore, to run SQL files from the command line using the psql command a .pgpass file must be created, properly configured, and formatted.
  		  
__Note:__ There is one inconsistency between the SQLite database and the PostgreSQL databaase.  Within the the SQLite database the *playlist_track* table has two PRIMARY KEYS, which is not supported in PostgreSQL.  As such that particular table has no primary key.  		  

#### Database chinook Schema
![chinook-schema](https://s3.amazonaws.com/dq-content/189/chinook-schema.svg)