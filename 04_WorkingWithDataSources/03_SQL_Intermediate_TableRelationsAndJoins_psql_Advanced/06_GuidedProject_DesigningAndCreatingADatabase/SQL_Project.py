
# coding: utf-8

# ## <font color=blue>01 Getting to Know the Data</font>
#   -  Using pandas, read in each of the four CSV files: <font color=red>game_log.csv, park_codes.csv, person_codes.csv, team_codes.csv</font>. For each:
#     -  Use methods and attributes like <font color=red>DataFrame.shape, DataFrame.head()</font>, and <font color=red>DataFrame.tail()</font> to explore the data.
#     -  Write a brief paragraph to describe each file, including for the helper files how the data intersects with the main log file.
#   -  Research any fields you are not familiar with, using both the text file and Google as needed. In particular, you should explore and write a short paragraph on:
#     -  What each defensive position number represents.
#     -  The values in the various league fields, and which leagues they represent.

# In[1]:


# %matplotlib inline
import pandas as pd
import sqlite3

pd.set_option('max_columns', 180)
pd.set_option('max_rows', 200000)
pd.set_option('max_colwidth', 5000)

game_log = pd.read_csv('game_log.csv')
park_codes = pd.read_csv('park_codes.csv')
person_codes = pd.read_csv('person_codes.csv')
team_codes = pd.read_csv('team_codes.csv')


# In[2]:


print('Explore game_log data')
print('\ngame_log data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=game_log.shape[0], cols=game_log.shape[1]))
print('\ngame_log columns')
for col in game_log.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of game_log*****\n')
print(game_log.head(3))
print('\n\n\n*****Last 3 rows of game_log*****\n')
print(game_log.tail(3))


# In[3]:


get_ipython().system('cat game_log_fields.txt')


# ### <font color=blue>game_log Data Set description</font>
#   1.  Columns: 161
#   1.  Rows: 171,907
#   1.  It looks like the combination of the <font color=red>*date*, *v_game_number*</font>, & <font color=red>*h_game_number*</font> columns can be used to make a PRIMARY KEY.
#   1.  Columns 1 - 19 describe the game numbers, teams, datetime, the statium, ect...
#   1.  Columns 20 - 161 have metrics that describe game play such as hit, home runs, doubles, ect...

# In[4]:


print('Explore park_codes data')
print('\npark_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=park_codes.shape[0], cols=park_codes.shape[1]))
print('\npark_codes columns')
for col in park_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of park_codes*****\n')
print(park_codes.head(3))
print('\n\n\n*****Last 3 rows of park_codes*****\n')
print(park_codes.tail(3))
print('\n\n\n****Lets Compare Park Codes from game_log*****\n')
print(game_log['park_id'].head(10))


# ### <font color=blue>park_codes Data Set description</font>
#   1.  Columns: 9
#   1.  Rows: 252
#   1.  It looks like the <font color=red>*park_id*</font> column can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
#   1.  All of the columns have basic information to describe each park

# In[5]:


print('Explore person_codes data')
print('\nperson_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=person_codes.shape[0], cols=person_codes.shape[1]))
print('\nperson_codes columns')
for col in person_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of person_codes*****\n')
print(person_codes.head(3))
print('\n\n\n*****Last 3 rows of person_codes*****\n')
print(person_codes.tail(3))


# ### <font color=blue>person_codes Data Set description</font>
#   1.  Columns: 7
#   1.  Rows: 20494
#   1.  It looks like the <font color=red>*id*</font> column can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
#   1.  However, the relationship looks to be a bit more complex than in many cases.  There are a multidue of columns were the game_log data set refererences a persion via their id.  Any time a given statistic in a game is linked back to a specific person their person_codes id is utilized.
#   1.  The person_codes columns provide the person's first and last names.  As well as their debut dates as a player, manager, coach, or ump.

# In[6]:


print('Explore team_codes data')
print('\nteam_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=team_codes.shape[0], cols=team_codes.shape[1]))

print(team_codes['team_id'].value_counts())
print(team_codes['team_id'].value_counts().shape)
print(team_codes[team_codes['team_id'] == 'MIL'])

print('\nteam_codes columns')
for col in team_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of team_codes*****\n')
print(team_codes.head(3))
print('\n\n\n*****Last 3 rows of team_codes*****\n')
print(team_codes.tail(3))


# ### <font color=blue>team_codes Data Set description</font>
#   1.  Columns: 8
#   1.  Rows: 150
#   1.  It looks like the <font color=red>*team_id*</font> and  <font color=red>*league*</font> columns can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
#   1.  The relationship can be made between the team_codes.team_id column and the  game_log.v_name and game_log.v_league or game_log.h_name and game_log.h_league columns.
#   1.  Furthermore, a recursive relationship exists using the franch_id.  It is necessary because it some franchises have have multiple entries if they've switched from one league to another.
#     1.  I noticed this with MIL, however the Houston Astros are another team that has switch leagues, but that is not captured in this dataset.  Perhaps the data set is not up to date.
#   1.  The team_codes has some basic info on each team:
#     1.  Team foundation and terminations dates
#     1.  league
#     1.  Location
#     1.  Nickname
#     1.  I'm not sure what the seq columns is for.

# ## <font color=blue>02 Importing Data into SQLite</font>
#   -  Recreate the <font color=red>*run_command()*</font> and <font color=red>*run_query()*</font> functions from the previous guided project, which you can use.
#   -  Use <font color=red>*DataFrame.to_sql()*</font> to create tables for each of our dataframes in a new SQLite database, <font color=red>*mlb.db*</font>:
#     -  The table name should be the same as each of the CSV filename without the extension, eg <font color=red>*game_log.csv*</font> should be imported to a table called <font color=red>*game_log*</font>.
#   -  Using <font color=red>*run_command()*</font>, create a new column in the <font color=red>*game_log*</font> table called <font color=red>*game_id*</font>. The following game_log columns should be conconated:
#     1.  <font color=red>*h_name*</font>
#     1.  <font color=red>*date*</font> in the following format (yyyymmdd)
#     1.  <font color=red>*number_of_game*</font>
#     1.  Here's an example of the conconated column (Atlanta Braves - April 8, 1983 - Game 0):
#       *  ATL198304080

# In[7]:


def run_query(query):
    with sqlite3.connect('mlb.db') as conn:
        return pd.read_sql_query(query, conn)

def run_command(command):
    with sqlite3.connect('mlb.db') as conn:
        conn.isolation_level = None # tells SQLite to autocommit any changes
        conn.execute(command)
        
def create_DF_table(df, tablename):
    with sqlite3.connect('mlb.db') as conn:
        conn.execute("DROP TABLE IF EXISTS {};".format(tablename))
        df.to_sql(tablename, conn, flavor='sqlite', index=False)

def show_tables():
    with sqlite3.connect('mlb.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [str('%s' % x) for x in cur.fetchall()]
    
def show_columns(tablename):
    # This work but it's too easy to over load Jupyter Notebook
    with sqlite3.connect('mlb.db') as conn:
        conn.isolation_level = None # tells SQLite to autocommit any changes
        column_query = conn.execute('SELECT * from {tab};'.format(tab=tablename))
        return [description[0] for description in column_query.description]


# In[8]:


create_DF_table(game_log, 'game_log')
create_DF_table(park_codes, 'park_codes')
create_DF_table(person_codes, 'person_codes')
create_DF_table(team_codes, 'team_codes')


# In[9]:


tables = show_tables()
for t in tables:
    print(t)


# In[10]:


run_command('ALTER TABLE game_log ADD COLUMN game_id TEXT;')

update_query = '''
UPDATE game_log 
SET game_id = h_name || date || number_of_game
WHERE game_id IS Null;
'''
run_command(update_query)
run_query('SELECT game_id, h_name, date, number_of_game                 FROM game_log LIMIT 10;')


# ## <font color=blue>03 Looing for Normalization Opportunities</font>
#   -  Looking at the various files, look for opportunities to normalize the data and record your observations in a markdown cell.
#   
# #### <font color=blue>The following are opportunities for normalization of our data:</font>
#   -  In person_codes, all the debut dates will be able to be reproduced using game log data.
#   -  In team_codes, the start, end and sequence columns will be able to be reproduced using game log data.
#   -  In park_codes, the start and end years will be able to be reproduced using game log data. While technically the state is an attribute of the city, we might not want to have a an incomplete city/state table so we will leave this in.
#   -  There are lots of places in game log where we have a player ID followed by the players name. We will be able to remove this and use the name data in person_codes
#   -  In game_log, all offensive and defensive stats are repeated for the home team and the visiting team. We could break these out and have a table that lists each game twice, one for each team, and cut out this column repetition.
#   -  Similarly, in game_log, we have a listing for 9 players on each team with their positions - we can remove these and have one table that tracks player appearances and their positions.
#   -  We can do a similar thing with the umpires from game_log, instead of listing all four positions as columns, we can put the umpires either in their own table or make one table for players, umpires and managers.
#   -  We have several awards in game_log like winning pitcher and losing pitcher. We can either break these out into their own table, have a table for awards, or combine the awards in with general appearances like the players and umpires.

# ## <font color=blue>04 Planning a Normalized Schema</font>
# 
# The best way to work visually with a schema diagram, just like the ones we've used so far in this course. Start by creating a diagram of the four existing tables and their columns, and then gradually create new tables that move the data into a more normalized state.
# 
# Some people like to do this on paper, others use diagramming tools like Sketch or Figma, others like using Photoshop or similar. Our recommendation is that the best way to do this is using a schema designing tool like [DbDesigner.net](https://dbdesigner.net/). This free tool allows you to create a schema and will create lines to show foreign key relations clearly.
# 
# #### <font color=blue>mlb DB Normalized Schema</font>
# 
# ![mlb.db Schema](https://s3.amazonaws.com/dq-content/193/mlb_schema.svg)

# ## <font color=blue>05 Create Tables w/o Foreign Relations</font>
#   -  Create the <font color=red>*person*</font> table with columns and primary key as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Insert the data from the <font color=red>*person_codes*</font> table.
#     -  Write a query to display the first few rows of the table.
#   -  Create the <font color=red>*park*</font> table with columns and primary key as shown in the schema diagram.
#     -  Select the appropriate type based on the data
#     -  Insert the data from the <font color=red>*park_codes*</font> table.
#     -  Write a query to display the first few rows of the table.
#   -  Create the <font color=red>*league*</font> table with columns and primary key as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Insert the data manually based on your research on the names of the six league IDs.
#     -  Write a query to display the table.
#   -  Create the <font color=red>*appearance_type*</font> table with columns and primary key as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Import and insert the data from <font color=red>*appearance_type.csv*</font>.
#     -  Write a query to display the table.
