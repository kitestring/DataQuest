
# coding: utf-8

# ## <font color=blue>01 Introduction to the Data</font>
# ### <font color=black>Let's first get everything you need setup.</font>
# -  <font color=black>Import sqlite3 into the environment.</font>
# -  <font color=black>Connect to nominations.db and assign the Connection instance to conn.</font>
# 
# ### <font color=black>Let's now write and run some queries to explore the data.</font>
# -  <font color=black>Return the schema using pragma table_info() and assign to schema.</font>
# -  <font color=black>Return the first 10 rows using the SELECT and LIMIT statements and assign to first_ten.</font>
# -  <font color=black>Since both schema and first_ten are lists, use a for loop to iterate over each element and print each element. This makes our output easier to understand.</font>

# In[1]:

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


# In[2]:

q_10Rows_nominations = 'SELECT * FROM nominations LIMIT 10'
first_tenDF = pd.read_sql_query(q_10Rows_nominations, conn)
first_ten = conn.execute(q_10Rows_nominations).fetchall()

for line in first_ten:
    print(line)
first_tenDF


# ## <font color=blue>02 Creating the ceremonies table.</font>
# ### <font color=black>Create the ceremonies table with the following schema:</font>
# -  <font color=black>id: integer, primary key</font>
# -  <font color=black>Year: integer</font>
# -  <font color=black>Host: text</font>
# 
# ### <font color=black>Create the list of tuples, years_hosts, that contains the values for the rows we want to insert into the ceremonies table.</font>
# ### <font color=black>Use the Connection method executemany to insert the values into the ceremonies table.</font>
# 
# ### <font color=black>To verify that the ceremonies table was created and populated correctly, run the following queries:</font>
# -  <font color=black>Return the first 10 rows using the SELECT and LIMIT statements.</font>
# -  <font color=black>Return the schema using pragma table_info().</font>

# In[3]:

q_create_ceremonies = '''CREATE TABLE ceremonies
    (id INTEGER PRIMARY KEY,
    Year Integer,
    Host TEXT);'''
conn.execute(q_create_ceremonies)

q4 = 'PRAGMA table_info(ceremonies)'
ceremoniesschemaDF = pd.read_sql_query(q4, conn)
print('Display Schema of ceremonies table')
ceremoniesschemaDF


# In[4]:

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


# In[5]:

verify_ceremonies_query = 'Select * FROM ceremonies'
ceremoniesDF = pd.read_sql_query(verify_ceremonies_query, conn)
print('Ceremonies Table')
ceremoniesDF


# ## <font color=blue>03 Foreign key constraints</font>
# ### <font color=black>Turn on foreign key constraints by writing and running the following query:</font>
# ##### <font color=black>PRAGMA foreign_keys = ON;</font>
# -  <font color=black>Since we'll be creating relations using foreign keys, we need to turn on foreign key constraints. By default, if you insert a row into a table that contains one or multiple foreign key columns, the record will be successfully inserted even if the foreign key reference is incorrect.</font>
# -  <font color=black>To prevent us from inserting rows with nonexisting foreign key values, we need to turn on foreign key constraints by running the following query: **PRAGMA foreign_keys = ON;**</font>

# In[6]:

conn.execute("PRAGMA foreign_keys = ON;")


# ## <font color=blue>04 Setting up one-to-many</font>
# ### <font color=black>Provided Instructions.</font>
# ##### <font color=black>Write and run the query to create the nominations_two table with the schema specified above.</font>
# ##### <font color=black>Write and run the query we discussed above that returns the records from the nominations table and assign the results set to joined_nominations.</font>
# ##### <font color=black>Write a placeholder insert query that can insert values into nominations_two and assign this query to insert_nominations_two. Make sure the ordering of the columns matches the ordering from joined_nominations.</font>
# ##### <font color=black>Use the Connection method executemany to insert the records in joined_nominations using the placeholder insert query insert_nominations_two.</font>
# ##### <font color=black>Verify your work by returning the first 5 rows from nominations_two.</font>
# ### <font color=black>Simpler Instructions.</font>
# ##### <font color=black>create a new table nominations_two with the schema we want,</font>
# ##### <font color=black>populate nominations_two with the records we want,</font>
# ##### <font color=black>delete the original nominations table,</font>
# ##### <font color=black>rename nominations_two to nominations.</font>

# In[7]:

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


# In[8]:

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


# In[9]:

print('nominations_two check')
nominations_two_check_query = 'SELECT * FROM nominations_two LIMIT 5;'
nominations_two_checkDF = pd.read_sql_query(nominations_two_check_query, conn)
nominations_two_checkDF


# In[10]:

drop_nominations_query = 'DROP TABLE nominations;'
conn.execute(drop_nominations_query)

rename_nominations_two_query = 'ALTER TABLE nominations_two RENAME TO nominations;'
conn.execute(rename_nominations_two_query)


# In[11]:

print('renamed nominations table check')
nominations_two_check_query = 'SELECT * FROM nominations LIMIT 5;'
nominations_checkDF = pd.read_sql_query(nominations_two_check_query, conn)
nominations_checkDF


# ## <font color=blue>05 Deleting and renaming tables</font>
# ##### <font color=black>Write and run the query that deletes the nominations table from the database.</font>
# ##### <font color=black>Write and run the query that renames nominations_two to nominations.</font>
# -  <font color=black>Note, these steps have already been done as part of step 04 Setting up one-to-many.</font>
# 

# ## <font color=blue>06 Creating a join table</font>
# ##### <font color=black>Create the 3 tables we need to model the relationship between movies and actors. You need to create the __movies__ and __actors__ tables before creating the __movies_actors__ table for the foreign key references to work.</font>
# ##### <font color=black>Create the __movies__ table using the following schema:</font>
# -  <font color=black>__id__: primary key, integer type</font>
# -  <font color=black>__movie__: movie name, text type</font>
# 
# ##### <font color=black>Create the __actors__ table using the following schema:</font>
# -  <font color=black>__id__: primary key, integer type</font>
# -  <font color=black>__actor__: actor's full name, text type</font>
# 
# ##### <font color=black>Create the __movies_actors__ join table using the following schema:</font>
# -  <font color=black>__id__: primary key, integer type</font>
# -  <font color=black>__movie_id__: foreign key reference to __movies.id__ column</font>
# -  <font color=black>__actor_id__: foreign key reference to __actors.id__ column</font>

# In[12]:

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


# In[13]:

conn.close()

