
# coding: utf-8

# ## <font color=blue>01 Getting to Know the Data</font>
#   -  Using pandas, read in each of the four CSV files: <font color=red>game_log.csv, park_codes.csv, person_codes.csv, team_codes.csv</font>. For each:
#     -  Use methods and attributes like <font color=red>DataFrame.shape, DataFrame.head()</font>, and <font color=red>DataFrame.tail()</font> to explore the data.
#     -  Write a brief paragraph to describe each file, including for the helper files how the data intersects with the main log file.
#   -  Research any fields you are not familiar with, using both the text file and Google as needed. In particular, you should explore and write a short paragraph on:
#     -  What each defensive position number represents.
#     -  The values in the various league fields, and which leagues they represent.

# In[2]:


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


# In[3]:


print('Explore game_log data')
print('\ngame_log data set size\n\tRows: {rows}\n\tCols: {cols}'.format(rows=game_log.shape[0], cols=game_log.shape[1]))
print('\ngame_log columns')
for col in game_log.columns:
    print('\t- ' + col)
print('\n\n\n*****First 3 rows of game_log*****\n')
print(game_log.head(3))
print('\n\n\n*****Last 3 rows of game_log*****\n')
print(game_log.tail(3))


# In[4]:


get_ipython().system('cat game_log_fields.txt')


# ### <font color=blue>game_log Data Set description</font>
#   1.  Columns: 161
#   1.  Rows: 171,907
#   1.  It looks like the combination of the <font color=red>*date*, *v_game_number*</font>, & <font color=red>*h_game_number*</font> columns can be used to make a PRIMARY KEY.
#   1.  Columns 1 - 19 describe the game numbers, teams, datetime, the statium, ect...
#   1.  Columns 20 - 161 have metrics that describe game play such as hit, home runs, doubles, ect...

# In[5]:


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

# In[6]:


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

# In[7]:


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

# In[8]:


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


# In[9]:


create_DF_table(game_log, 'game_log')
create_DF_table(park_codes, 'park_codes')
create_DF_table(person_codes, 'person_codes')
create_DF_table(team_codes, 'team_codes')


# In[10]:


tables = show_tables()
for t in tables:
    print(t)


# In[11]:


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

# In[12]:


c1 = """
CREATE TABLE IF NOT EXISTS person (
    person_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
"""

c2 = """
INSERT OR IGNORE INTO person
SELECT
    id,
    first,
    last
FROM person_codes;
"""

q = """
SELECT * FROM person
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)


# In[13]:


c1 = """
CREATE TABLE IF NOT EXISTS park (
    park_id TEXT PRIMARY KEY,
    name TEXT,
    nickname TEXT,
    city TEXT,
    state TEXT,
    notes TEXT
);
"""

c2 = """
INSERT OR IGNORE INTO park
SELECT
    park_id,
    name,
    aka,
    city,
    state,
    notes
FROM park_codes;
"""

q = """
SELECT * FROM park
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)


# In[14]:


c1 = """
CREATE TABLE IF NOT EXISTS league (
    league_id TEXT PRIMARY KEY,
    name TEXT
);
"""

c2 = """
INSERT OR IGNORE INTO league
VALUES
    ("NL", "National League"),
    ("AL", "American League"),
    ("AA", "American Association"),
    ("FL", "Federal League"),
    ("PL", "Players League"),
    ("UA", "Union Association")
;
"""

q = """
SELECT * FROM league
"""

run_command(c1)
run_command(c2)
run_query(q)


# In[15]:


c1 = "DROP TABLE IF EXISTS appearance_type;"

run_command(c1)

c2 = """
CREATE TABLE appearance_type (
    appearance_type_id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT
);
"""
run_command(c2)

appearance_type = pd.read_csv('appearance_type.csv')

with sqlite3.connect('mlb.db') as conn:
    appearance_type.to_sql('appearance_type',
                           conn,
                           index=False,
                           if_exists='append')

q = """
SELECT * FROM appearance_type;
"""

run_query(q)


# ## <font color=blue>06 Adding The Team and Game Tables</font>
#   -  Create the team <font color=red>*table*</font> with columns, primary key, and foreign key as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Insert the data from the <font color=red>*team_codes*</font> table.
#     -  Write a query to display the first few rows of the table.
#   -  Create the <font color=red>*game table*</font> with columns, primary key, and foreign key as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Insert the data from the <font color=red>*game_log*</font> table.
#     -  Write a query to display the first few rows of the table.

# In[16]:


c1 = """
CREATE TABLE IF NOT EXISTS team (
    team_id TEXT PRIMARY KEY,
    league_id TEXT,
    city TEXT,
    nickname TEXT,
    franch_id TEXT,
    FOREIGN KEY (league_id) REFERENCES league(league_id)
);
"""

c2 = """
INSERT OR IGNORE INTO team
SELECT
    team_id,
    league,
    city,
    nickname,
    franch_id
FROM team_codes;
"""

q = """
SELECT * FROM team
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)


# In[17]:


c1 = """
CREATE TABLE IF NOT EXISTS game (
    game_id TEXT PRIMARY KEY,
    date TEXT,
    number_of_game INTEGER,
    park_id TEXT,
    length_outs INTEGER,
    day BOOLEAN,
    completion TEXT,
    forefeit TEXT,
    protest TEXT,
    attendance INTEGER,
    legnth_minutes INTEGER,
    additional_info TEXT,
    acquisition_info TEXT,
    FOREIGN KEY (park_id) REFERENCES park(park_id)
);
"""

c2 = """
INSERT OR IGNORE INTO game
SELECT
    game_id,
    date,
    number_of_game,
    park_id,
    length_outs,
    CASE
        WHEN day_night = "D" THEN 1
        WHEN day_night = "N" THEN 0
        ELSE NULL
        END
        AS day,
    completion,
    forefeit,
    protest,
    attendance,
    length_minutes,
    additional_info,
    acquisition_info
FROM game_log;
"""

q = """
SELECT * FROM game
LIMIT 5;
"""

run_command(c1)
run_command(c2)
run_query(q)


# ## <font color=blue>07 Adding the Team Appearance Table</font>
#   -  Create the <font color=red>*team_appearance*</font> table with columns, primary key, and foreign keys as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Insert the data from the <font color=red>*game_log*</font> table, using a <font color=red>*UNION*</font> clause to combine the data from the column sets for the home and away teams.
#     -  Write a query to verify that your data was inserted correctly.

# In[18]:


c1 = """
CREATE TABLE IF NOT EXISTS team_appearance (
    team_id TEXT,
    game_id TEXT,
    home BOOLEAN,
    league_id TEXT,
    score INTEGER,
    line_score TEXT,
    at_bats INTEGER,
    hits INTEGER,
    doubles INTEGER,
    triples INTEGER,
    homeruns INTEGER,
    rbi INTEGER,
    sacrifice_hits INTEGER,
    sacrifice_flies INTEGER,
    hit_by_pitch INTEGER,
    walks INTEGER,
    intentional_walks INTEGER,
    strikeouts INTEGER,
    stolen_bases INTEGER,
    caught_stealing INTEGER,
    grounded_into_double INTEGER,
    first_catcher_interference INTEGER,
    left_on_base INTEGER,
    pitchers_used INTEGER,
    individual_earned_runs INTEGER,
    team_earned_runs INTEGER,
    wild_pitches INTEGER,
    balks INTEGER,
    putouts INTEGER,
    assists INTEGER,
    errors INTEGER,
    passed_balls INTEGER,
    double_plays INTEGER,
    triple_plays INTEGER,
    PRIMARY KEY (team_id, game_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);
"""

run_command(c1)

c2 = """
INSERT OR IGNORE INTO team_appearance
    SELECT
        h_name,
        game_id,
        1 AS home,
        h_league,
        h_score,
        h_line_score,
        h_at_bats,
        h_hits,
        h_doubles,
        h_triples,
        h_homeruns,
        h_rbi,
        h_sacrifice_hits,
        h_sacrifice_flies,
        h_hit_by_pitch,
        h_walks,
        h_intentional_walks,
        h_strikeouts,
        h_stolen_bases,
        h_caught_stealing,
        h_grounded_into_double,
        h_first_catcher_interference,
        h_left_on_base,
        h_pitchers_used,
        h_individual_earned_runs,
        h_team_earned_runs,
        h_wild_pitches,
        h_balks,
        h_putouts,
        h_assists,
        h_errors,
        h_passed_balls,
        h_double_plays,
        h_triple_plays
    FROM game_log

UNION

    SELECT    
        v_name,
        game_id,
        0 AS home,
        v_league,
        v_score,
        v_line_score,
        v_at_bats,
        v_hits,
        v_doubles,
        v_triples,
        v_homeruns,
        v_rbi,
        v_sacrifice_hits,
        v_sacrifice_flies,
        v_hit_by_pitch,
        v_walks,
        v_intentional_walks,
        v_strikeouts,
        v_stolen_bases,
        v_caught_stealing,
        v_grounded_into_double,
        v_first_catcher_interference,
        v_left_on_base,
        v_pitchers_used,
        v_individual_earned_runs,
        v_team_earned_runs,
        v_wild_pitches,
        v_balks,
        v_putouts,
        v_assists,
        v_errors,
        v_passed_balls,
        v_double_plays,
        v_triple_plays
    from game_log;
"""

run_command(c2)

q = """
SELECT * FROM team_appearance
WHERE game_id = (
                 SELECT MIN(game_id) from game
                )
   OR game_id = (
                 SELECT MAX(game_id) from game
                )
ORDER By game_id, home;
"""

run_query(q)


# ## <font color=blue>08 Adding the Person Appearance Table</font>
#   -  Create the <font color=red>*person_appearance*</font> table with columns, primary key, and foreign keys as shown in the schema diagram.
#     -  Select the appropriate type based on the data.
#     -  Insert the data from the <font color=red>*game_log*</font> table, using <font color=red>*UNION*</font> clauses to combine the data from the columns for managers, umpires, pitchers, and awards.
#     -  Use a loop with string formatting to insert the data for offensive and defensive positions from the <font color=red>*game_log*</font> table.
#     -  Write a query to verify that your data was inserted correctly.

# In[19]:


c0 = "DROP TABLE IF EXISTS person_appearance"

run_command(c0)

c1 = """
CREATE TABLE person_appearance (
    appearance_id INTEGER PRIMARY KEY,
    person_id TEXT,
    team_id TEXT,
    game_id TEXT,
    appearance_type_id,
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    FOREIGN KEY (team_id) REFERENCES team(team_id),
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (appearance_type_id) REFERENCES appearance_type(appearance_type_id)
);
"""

c2 = """
INSERT OR IGNORE INTO person_appearance (
    game_id,
    team_id,
    person_id,
    appearance_type_id
) 
    SELECT
        game_id,
        NULL,
        hp_umpire_id,
        "UHP"
    FROM game_log
    WHERE hp_umpire_id IS NOT NULL    

UNION

    SELECT
        game_id,
        NULL,
        [1b_umpire_id],
        "U1B"
    FROM game_log
    WHERE "1b_umpire_id" IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        [2b_umpire_id],
        "U2B"
    FROM game_log
    WHERE [2b_umpire_id] IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        [3b_umpire_id],
        "U3B"
    FROM game_log
    WHERE [3b_umpire_id] IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        lf_umpire_id,
        "ULF"
    FROM game_log
    WHERE lf_umpire_id IS NOT NULL

UNION

    SELECT
        game_id,
        NULL,
        rf_umpire_id,
        "URF"
    FROM game_log
    WHERE rf_umpire_id IS NOT NULL

UNION

    SELECT
        game_id,
        v_name,
        v_manager_id,
        "MM"
    FROM game_log
    WHERE v_manager_id IS NOT NULL

UNION

    SELECT
        game_id,
        h_name,
        h_manager_id,
        "MM"
    FROM game_log
    WHERE h_manager_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score > v_score THEN h_name
            ELSE v_name
            END,
        winning_pitcher_id,
        "AWP"
    FROM game_log
    WHERE winning_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score < v_score THEN h_name
            ELSE v_name
            END,
        losing_pitcher_id,
        "ALP"
    FROM game_log
    WHERE losing_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score > v_score THEN h_name
            ELSE v_name
            END,
        saving_pitcher_id,
        "ASP"
    FROM game_log
    WHERE saving_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        CASE
            WHEN h_score > v_score THEN h_name
            ELSE v_name
            END,
        winning_rbi_batter_id,
        "AWB"
    FROM game_log
    WHERE winning_rbi_batter_id IS NOT NULL

UNION

    SELECT
        game_id,
        v_name,
        v_starting_pitcher_id,
        "PSP"
    FROM game_log
    WHERE v_starting_pitcher_id IS NOT NULL

UNION

    SELECT
        game_id,
        h_name,
        h_starting_pitcher_id,
        "PSP"
    FROM game_log
    WHERE h_starting_pitcher_id IS NOT NULL;
"""

template = """
INSERT INTO person_appearance (
    game_id,
    team_id,
    person_id,
    appearance_type_id
) 
    SELECT
        game_id,
        {hv}_name,
        {hv}_player_{num}_id,
        "O{num}"
    FROM game_log
    WHERE {hv}_player_{num}_id IS NOT NULL

UNION

    SELECT
        game_id,
        {hv}_name,
        {hv}_player_{num}_id,
        "D" || CAST({hv}_player_{num}_def_pos AS INT)
    FROM game_log
    WHERE {hv}_player_{num}_id IS NOT NULL;
"""

run_command(c1)
run_command(c2)

for hv in ["h","v"]:
    for num in range(1,10):
        query_vars = {
            "hv": hv,
            "num": num
        }
        run_command(template.format(**query_vars))


# In[20]:


print(run_query("SELECT COUNT(DISTINCT game_id) games_game FROM game"))
print(run_query("SELECT COUNT(DISTINCT game_id) games_person_appearance FROM person_appearance"))

q = """
SELECT
    pa.*,
    at.name,
    at.category
FROM person_appearance pa
INNER JOIN appearance_type at on at.appearance_type_id = pa.appearance_type_id
WHERE PA.game_id = (
                   SELECT max(game_id)
                    FROM person_appearance
                   )
ORDER BY team_id, appearance_type_id
"""

run_query(q)


# ## <font color=blue>09 Removing the Original Tables</font>
#   -  Drop the tables we created to hold our unnormalized data:
#     -  <font color=red>*game_log*</font>
#     -  <font color=red>*park_codes*</font>
#     -  <font color=red>*team_codes*</font>
#     -  <font color=red>*person_codes*</font>

# In[21]:


show_tables()


# In[22]:


tables = [
    "game_log",
    "park_codes",
    "team_codes",
    "person_codes"
]

for t in tables:
    c = '''
    DROP TABLE {}
    '''.format(t)
    
    run_command(c)

show_tables()

