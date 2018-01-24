
# coding: utf-8

# ## <font color=blue>01 Getting to Know the Data</font>
#   -  Using pandas, read in each of the four CSV files: <font color=red>game_log.csv, park_codes.csv, person_codes.csv, team_codes.csv</font>. For each:
#     -  Use methods and attributes like <font color=red>DataFrame.shape, DataFrame.head()</font>, and <font color=red>DataFrame.tail()</font> to explore the data.
#     -  Write a brief paragraph to describe each file, including for the helper files how the data intersects with the main log file.
#   -  Research any fields you are not familiar with, using both the text file and Google as needed. In particular, you should explore and write a short paragraph on:
#     -  What each defensive position number represents.
#     -  The values in the various league fields, and which leagues they represent.

# In[23]:


get_ipython().magic('matplotlib inline')
import pandas as pd

pd.set_option('max_columns', 180)
pd.set_option('max_rows', 200000)
pd.set_option('max_colwidth', 5000)

game_log = pd.read_csv('game_log.csv')
park_codes = pd.read_csv('park_codes.csv')
person_codes = pd.read_csv('person_codes.csv')
team_codes = pd.read_csv('team_codes.csv')


# In[25]:


print('Explore game_log data')
print('\ngame_log data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=game_log.shape[0], cols=game_log.shape[1]))
print('\ngame_log columns')
for col in game_log.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of game_log*****\n')
print(game_log.head(3))
print('\n\n\n*****Last 3 rows of game_log*****\n')
print(game_log.tail(3))


# In[24]:


get_ipython().system('cat game_log_fields.txt')


# ### <font color=blue>game_log Data Set description</font>
#   1.  161 Columns
#   1.  171,907 Rows
#   1.  It looks like it the combination of the <font color=red>*date*, *v_game_number*</font>, & <font color=red>*h_game_number*</font> columns can be used to make a PRIMARY KEY.
#   1.  Columns 1 - 19 describe the game numbers, teams, datetime, the statium, ect...
#   1.  Columns 20 - 161 have metrics that describe game play such as hit, home runs, doubles, ect...

# In[29]:


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
#   1.  9 Columns
#   1.  252 Rows
#   1.  It looks like the <font color=red>*park_id*</font> column can be used to make a PRIMARY KEY and to create a relationship to the game_log data set.
#   1.  All of the columns have basic information to describe each park

# In[30]:


print('Explore person_codes data')
print('\nperson_codes data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=person_codes.shape[0], cols=person_codes.shape[1]))
print('\nperson_codes columns')
for col in person_codes.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of person_codes*****\n')
print(person_codes.head(3))
print('\n\n\n*****Last 3 rows of person_codes*****\n')
print(person_codes.tail(3))

