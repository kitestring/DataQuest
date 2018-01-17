### Procedure Change

The steps in this exercise are written for SQLite, and the chinook.db was provided.  To add an extra wrinkle the follwing alterations will be made to the steps to this exercise.
1.  A new module will be written with a class to extract the data from the chinook.db and load it into a PostgreSQL managed database.
1.  Then the remainder of the steps will be done usisng PostgreSQL rather than SQLite.
1.  Using the PostgreSQL command line the user ken_kite should be added with permisison to create databases.  The syntax for this will be saved on *"PostgreSQLCommandLine_Setup.txt"*.

__Note:__ There is one inconsistancy between the SQLite database and the PostgreSQL databaase.  Witin the the SQLite database the *playlist_track* table has two PRIMARY KEYS, which is not supported in PostgreSQL.  As such that particular table has no primary key.

### Database chinook Schema
![chinook-schema](https://s3.amazonaws.com/dq-content/189/chinook-schema.svg)

