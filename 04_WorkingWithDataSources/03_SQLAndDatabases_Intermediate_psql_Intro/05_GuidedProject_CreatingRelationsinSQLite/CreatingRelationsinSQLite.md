
## <font color=blue>01 Introduction to the Data</font>
### <font color=black>Let's first get everything you need setup.</font>
-  <font color=black>Import sqlite3 into the environment.</font>
-  <font color=black>Connect to nominations.db and assign the Connection instance to conn.</font>

### <font color=black>Let's now write and run some queries to explore the data.</font>
-  <font color=black>Return the schema using pragma table_info() and assign to schema.</font>
-  <font color=black>Return the first 10 rows using the SELECT and LIMIT statements and assign to first_ten.</font>
-  <font color=black>Since both schema and first_ten are lists, use a for loop to iterate over each element and print each element. This makes our output easier to understand.</font>


```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('nominations.db')

q_SchemaCheck = 'PRAGMA table_info(nominations)'
nominationsschema = conn.execute(q_SchemaCheck).fetchall()
print('nominations table schema')

for s in nominationsschema:
    print(s)
    
nominationsschemaDF = pd.read_sql_query(q_SchemaCheck, conn)
nominationsschemaDF
```

    nominations table schema
    (0, 'Year', 'INTEGER', 0, None, 0)
    (1, 'Category', 'TEXT', 0, None, 0)
    (2, 'Nominee', 'TEXT', 0, None, 0)
    (3, 'Won', 'INTEGER', 0, None, 0)
    (4, 'Movie', 'TEXT', 0, None, 0)
    (5, 'Character', 'TEXT', 0, None, 0)
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cid</th>
      <th>name</th>
      <th>type</th>
      <th>notnull</th>
      <th>dflt_value</th>
      <th>pk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Year</td>
      <td>INTEGER</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Category</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Nominee</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Won</td>
      <td>INTEGER</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Movie</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Character</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
q_10Rows_nominations = 'SELECT * FROM nominations LIMIT 10'
first_tenDF = pd.read_sql_query(q_10Rows_nominations, conn)
first_ten = conn.execute(q_10Rows_nominations).fetchall()

for line in first_ten:
    print(line)
first_tenDF
```

    (2010, 'Actor -- Leading Role', 'Javier Bardem', 0, 'Biutiful', 'Uxbal')
    (2010, 'Actor -- Leading Role', 'Jeff Bridges', 0, 'True Grit', 'Rooster Cogburn')
    (2010, 'Actor -- Leading Role', 'Jesse Eisenberg', 0, 'The Social Network', 'Mark Zuckerberg')
    (2010, 'Actor -- Leading Role', 'Colin Firth', 1, "The King's Speech", 'King George VI')
    (2010, 'Actor -- Leading Role', 'James Franco', 0, '127 Hours', 'Aron Ralston')
    (2010, 'Actor -- Supporting Role', 'Christian Bale', 1, 'The Fighter', 'Dicky Eklund')
    (2010, 'Actor -- Supporting Role', 'John Hawkes', 0, "Winter's Bone", 'Teardrop')
    (2010, 'Actor -- Supporting Role', 'Jeremy Renner', 0, 'The Town', 'James Coughlin')
    (2010, 'Actor -- Supporting Role', 'Mark Ruffalo', 0, 'The Kids Are All Right', 'Paul')
    (2010, 'Actor -- Supporting Role', 'Geoffrey Rush', 0, "The King's Speech", 'Lionel Logue')
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Category</th>
      <th>Nominee</th>
      <th>Won</th>
      <th>Movie</th>
      <th>Character</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010</td>
      <td>Actor -- Leading Role</td>
      <td>Javier Bardem</td>
      <td>0</td>
      <td>Biutiful</td>
      <td>Uxbal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010</td>
      <td>Actor -- Leading Role</td>
      <td>Jeff Bridges</td>
      <td>0</td>
      <td>True Grit</td>
      <td>Rooster Cogburn</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010</td>
      <td>Actor -- Leading Role</td>
      <td>Jesse Eisenberg</td>
      <td>0</td>
      <td>The Social Network</td>
      <td>Mark Zuckerberg</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2010</td>
      <td>Actor -- Leading Role</td>
      <td>Colin Firth</td>
      <td>1</td>
      <td>The King's Speech</td>
      <td>King George VI</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2010</td>
      <td>Actor -- Leading Role</td>
      <td>James Franco</td>
      <td>0</td>
      <td>127 Hours</td>
      <td>Aron Ralston</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2010</td>
      <td>Actor -- Supporting Role</td>
      <td>Christian Bale</td>
      <td>1</td>
      <td>The Fighter</td>
      <td>Dicky Eklund</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2010</td>
      <td>Actor -- Supporting Role</td>
      <td>John Hawkes</td>
      <td>0</td>
      <td>Winter's Bone</td>
      <td>Teardrop</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2010</td>
      <td>Actor -- Supporting Role</td>
      <td>Jeremy Renner</td>
      <td>0</td>
      <td>The Town</td>
      <td>James Coughlin</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2010</td>
      <td>Actor -- Supporting Role</td>
      <td>Mark Ruffalo</td>
      <td>0</td>
      <td>The Kids Are All Right</td>
      <td>Paul</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>Actor -- Supporting Role</td>
      <td>Geoffrey Rush</td>
      <td>0</td>
      <td>The King's Speech</td>
      <td>Lionel Logue</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>02 Creating the ceremonies table.</font>
### <font color=black>Create the ceremonies table with the following schema:</font>
-  <font color=black>id: integer, primary key</font>
-  <font color=black>Year: integer</font>
-  <font color=black>Host: text</font>

### <font color=black>Create the list of tuples, years_hosts, that contains the values for the rows we want to insert into the ceremonies table.</font>
### <font color=black>Use the Connection method executemany to insert the values into the ceremonies table.</font>

### <font color=black>To verify that the ceremonies table was created and populated correctly, run the following queries:</font>
-  <font color=black>Return the first 10 rows using the SELECT and LIMIT statements.</font>
-  <font color=black>Return the schema using pragma table_info().</font>


```python
q_create_ceremonies = '''CREATE TABLE ceremonies
    (id INTEGER PRIMARY KEY,
    Year Integer,
    Host TEXT);'''
conn.execute(q_create_ceremonies)

q4 = 'PRAGMA table_info(ceremonies)'
ceremoniesschemaDF = pd.read_sql_query(q4, conn)
print('Display Schema of ceremonies table')
ceremoniesschemaDF
```

    Display Schema of ceremonies table
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cid</th>
      <th>name</th>
      <th>type</th>
      <th>notnull</th>
      <th>dflt_value</th>
      <th>pk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>id</td>
      <td>INTEGER</td>
      <td>0</td>
      <td>None</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Year</td>
      <td>Integer</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Host</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
years_hosts = [(2010, "Steve Martin"),
               (2009, "Hugh Jackman"),
               (2008, "Jon Stewart"),
               (2007, "Ellen DeGeneres"),
               (2006, "Jon Stewart"),
               (2005, "Chris Rock"),
               (2004, "Billy Crystal"),
               (2003, "Steve Martin"),
               (2002, "Whoopi Goldberg"),
               (2001, "Steve Martin"),
               (2000, "Billy Crystal"),
            ]
InsertHostData_query = "INSERT INTO ceremonies (Year, Host) VALUES (?,?);"
conn.executemany(InsertHostData_query, years_hosts)
```




    <sqlite3.Cursor at 0x20543e86c00>




```python
verify_ceremonies_query = 'Select * FROM ceremonies'
ceremoniesDF = pd.read_sql_query(verify_ceremonies_query, conn)
print('Ceremonies Table')
ceremoniesDF
```

    Ceremonies Table
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>Year</th>
      <th>Host</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2010</td>
      <td>Steve Martin</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2009</td>
      <td>Hugh Jackman</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2008</td>
      <td>Jon Stewart</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2007</td>
      <td>Ellen DeGeneres</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2006</td>
      <td>Jon Stewart</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>2005</td>
      <td>Chris Rock</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>2004</td>
      <td>Billy Crystal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>2003</td>
      <td>Steve Martin</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>2002</td>
      <td>Whoopi Goldberg</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>2001</td>
      <td>Steve Martin</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>2000</td>
      <td>Billy Crystal</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>03 Foreign key constraints</font>
### <font color=black>Turn on foreign key constraints by writing and running the following query:</font>
##### <font color=black>PRAGMA foreign_keys = ON;</font>
-  <font color=black>Since we'll be creating relations using foreign keys, we need to turn on foreign key constraints. By default, if you insert a row into a table that contains one or multiple foreign key columns, the record will be successfully inserted even if the foreign key reference is incorrect.</font>
-  <font color=black>To prevent us from inserting rows with nonexisting foreign key values, we need to turn on foreign key constraints by running the following query: **PRAGMA foreign_keys = ON;**</font>


```python
conn.execute("PRAGMA foreign_keys = ON;")
```




    <sqlite3.Cursor at 0x20543e86a40>



## <font color=blue>04 Setting up one-to-many</font>
### <font color=black>Provided Instructions.</font>
##### <font color=black>Write and run the query to create the nominations_two table with the schema specified above.</font>
##### <font color=black>Write and run the query we discussed above that returns the records from the nominations table and assign the results set to joined_nominations.</font>
##### <font color=black>Write a placeholder insert query that can insert values into nominations_two and assign this query to insert_nominations_two. Make sure the ordering of the columns matches the ordering from joined_nominations.</font>
##### <font color=black>Use the Connection method executemany to insert the records in joined_nominations using the placeholder insert query insert_nominations_two.</font>
##### <font color=black>Verify your work by returning the first 5 rows from nominations_two.</font>
### <font color=black>Simpler Instructions.</font>
##### <font color=black>create a new table nominations_two with the schema we want,</font>
##### <font color=black>populate nominations_two with the records we want,</font>
##### <font color=black>delete the original nominations table,</font>
##### <font color=black>rename nominations_two to nominations.</font>


```python
print('Create Temporary Table: nominations_two\n')
create_nominations_two = '''CREATE TABLE nominations_two
    (id INTEGER PRIMARY KEY,
    category TEXT,
    nominee TEXT,
    movie TEXT,
    character TEXT,
    won INTEGER,
    cermony_id INTEGER,
    FOREIGN KEY(cermony_id) REFERENCES ceremonies(id));'''
conn.execute(create_nominations_two)

nominations_two_schema_query = 'PRAGMA table_info(nominations_two)'
nominations_two_schemaDF = pd.read_sql_query(nominations_two_schema_query, conn)

print('Display Schema of temporary table: nominations_two')
nominations_two_schemaDF
```

    Create Temporary Table: nominations_two
    
    Display Schema of temporary table: nominations_two
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cid</th>
      <th>name</th>
      <th>type</th>
      <th>notnull</th>
      <th>dflt_value</th>
      <th>pk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>id</td>
      <td>INTEGER</td>
      <td>0</td>
      <td>None</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>category</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>nominee</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>movie</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>character</td>
      <td>TEXT</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>won</td>
      <td>INTEGER</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>cermony_id</td>
      <td>INTEGER</td>
      <td>0</td>
      <td>None</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
nominations_two_query = '''SELECT 
    nominations.category, 
    nominations.nominee, 
    nominations.movie, 
    nominations.character, 
    nominations.won, 
    ceremonies.id
FROM nominations
INNER JOIN ceremonies ON
nominations.year == ceremonies.year;'''
nominations_two_datarows = conn.execute(nominations_two_query).fetchall()

Insertnominations_two_query = '''
    INSERT INTO nominations_two (category, nominee, movie, 
    character, won, cermony_id) VALUES (?,?,?,?,?,?);'''

conn.executemany(Insertnominations_two_query, nominations_two_datarows)
```




    <sqlite3.Cursor at 0x20543e86b20>




```python
print('nominations_two check')
nominations_two_check_query = 'SELECT * FROM nominations_two LIMIT 5;'
nominations_two_checkDF = pd.read_sql_query(nominations_two_check_query, conn)
nominations_two_checkDF
```

    nominations_two check
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>category</th>
      <th>nominee</th>
      <th>movie</th>
      <th>character</th>
      <th>won</th>
      <th>cermony_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Actor -- Leading Role</td>
      <td>Javier Bardem</td>
      <td>Biutiful</td>
      <td>Uxbal</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Actor -- Leading Role</td>
      <td>Jeff Bridges</td>
      <td>True Grit</td>
      <td>Rooster Cogburn</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Actor -- Leading Role</td>
      <td>Jesse Eisenberg</td>
      <td>The Social Network</td>
      <td>Mark Zuckerberg</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Actor -- Leading Role</td>
      <td>Colin Firth</td>
      <td>The King's Speech</td>
      <td>King George VI</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Actor -- Leading Role</td>
      <td>James Franco</td>
      <td>127 Hours</td>
      <td>Aron Ralston</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
drop_nominations_query = 'DROP TABLE nominations;'
conn.execute(drop_nominations_query)

rename_nominations_two_query = 'ALTER TABLE nominations_two RENAME TO nominations;'
conn.execute(rename_nominations_two_query)
```




    <sqlite3.Cursor at 0x20543e86f80>




```python
print('renamed nominations table check')
nominations_two_check_query = 'SELECT * FROM nominations LIMIT 5;'
nominations_checkDF = pd.read_sql_query(nominations_two_check_query, conn)
nominations_checkDF
```

    renamed nominations table check
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>category</th>
      <th>nominee</th>
      <th>movie</th>
      <th>character</th>
      <th>won</th>
      <th>cermony_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Actor -- Leading Role</td>
      <td>Javier Bardem</td>
      <td>Biutiful</td>
      <td>Uxbal</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Actor -- Leading Role</td>
      <td>Jeff Bridges</td>
      <td>True Grit</td>
      <td>Rooster Cogburn</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Actor -- Leading Role</td>
      <td>Jesse Eisenberg</td>
      <td>The Social Network</td>
      <td>Mark Zuckerberg</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Actor -- Leading Role</td>
      <td>Colin Firth</td>
      <td>The King's Speech</td>
      <td>King George VI</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Actor -- Leading Role</td>
      <td>James Franco</td>
      <td>127 Hours</td>
      <td>Aron Ralston</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>05 Deleting and renaming tables</font>
##### <font color=black>Write and run the query that deletes the nominations table from the database.</font>
##### <font color=black>Write and run the query that renames nominations_two to nominations.</font>
-  <font color=black>Note, these steps have already been done as part of step 04 Setting up one-to-many.</font>


## <font color=blue>06 Creating a join table</font>
##### <font color=black>Create the 3 tables we need to model the relationship between movies and actors. You need to create the __movies__ and __actors__ tables before creating the __movies_actors__ table for the foreign key references to work.</font>
##### <font color=black>Create the __movies__ table using the following schema:</font>
-  <font color=black>__id__: primary key, integer type</font>
-  <font color=black>__movie__: movie name, text type</font>

##### <font color=black>Create the __actors__ table using the following schema:</font>
-  <font color=black>__id__: primary key, integer type</font>
-  <font color=black>__actor__: actor's full name, text type</font>

##### <font color=black>Create the __movies_actors__ join table using the following schema:</font>
-  <font color=black>__id__: primary key, integer type</font>
-  <font color=black>__movie_id__: foreign key reference to __movies.id__ column</font>
-  <font color=black>__actor_id__: foreign key reference to __actors.id__ column</font>


```python
create_movies_table = '''CREATE TABLE movies
    (id INTEGER PRIMARY KEY,
    movie TEXT);'''

create_actors_table = '''CREATE TABLE actors
    (id INTEGER PRIMARY KEY,
    actor TEXT);'''

create_movies_actors_table = '''CREATE TABLE movies_actors
    (id INTEGER PRIMARY KEY,
    movie_id INTEGER REFERENCES movies(id),
    actor_id INTEGER REFERENCES actors(id));'''

conn.execute(create_movies_table)
conn.execute(create_actors_table)
conn.execute(create_movies_actors_table)
```




    <sqlite3.Cursor at 0x20543e869d0>




```python
conn.close()
```
