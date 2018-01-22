
## <font color=blue>*chinook* DB Schema</font>
![chinook-schema](https://s3.amazonaws.com/dq-content/189/chinook-schema.svg)

# <font color=blue>Tips for writing complex queries<font>
-  <font color=black>Write your query in stages, and run it as you go to make sure at each stage it's producing the output you expect.</font>
-  <font color=black>If something isn't behaving as you expect, break parts of the query out into their own, separate queries to make sure there's not an inner logic error.</font>
-  <font color=black>Don't be afraid to write separate queries to check the underlying data, for instance you might write a query that you can use to manually check a calculation and give yourself confidence that the output you're seeing is correct.</font>
-  <font color=black>If you do get stuck, don't forget your support options.</font>

### <font color=blue>02 Creating Helper Functions</font>
-  <font color=black>Import the psycopg2, pandas and matplotlib modules, and use the magic command <font color=red>*%matplotlib*</font> inline to make sure any plots render in the notebook.</font>
-  <font color=black>Create a <font color=red>*run_query()*</font> function, that takes a SQL query as an argument and returns a pandas dataframe of that query.</font>
-  <font color=black>Create a <font color=red>*run_command()*</font> function that takes a SQL command as an argument and executes it using the sqlite module.</font>
-  <font color=black>Create a <font color=red>*show_tables()*</font> function that calls the <font color=red>*run_query()*</font> function to return a list of all tables and views in the database.</font>
-  <font color=black>Run the <font color=red>*show_tables()*</font> function.</font>


```python
%matplotlib
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import security as s


# cur = conn.cursor() 
```

    Using matplotlib backend: Qt5Agg



```python
def run_query(query):
    with psycopg2.connect(dbname='chinook', user=s.credentials['user'], 
                          host=s.credentials['host'], password=s.credentials['password']) as conn:
        
        return pd.read_sql_query(query, conn)

def run_command(command):
    with psycopg2.connect(dbname='chinook', user=s.credentials['user'], 
                          host=s.credentials['host'], password=s.credentials['password']) as conn:
        
        conn.isolation_level = None # tells PostgreSQL to autocommit any changes
        conn.execute(command)

def show_tables():
    with psycopg2.connect(dbname='chinook', user=s.credentials['user'], 
                          host=s.credentials['host'], password=s.credentials['password']) as conn:
        
        query = "select table_name, table_type from information_schema.tables \
                    where table_type = 'BASE TABLE' AND table_schema = 'public';"
        return run_query(query)

tables = show_tables()
tables
```




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
      <th>table_name</th>
      <th>table_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>album</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>1</th>
      <td>artist</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>customer</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>employee</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>4</th>
      <td>genre</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>5</th>
      <td>invoice</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>6</th>
      <td>invoice_line</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>7</th>
      <td>media_type</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>8</th>
      <td>playlist</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>9</th>
      <td>playlist_track</td>
      <td>BASE TABLE</td>
    </tr>
    <tr>
      <th>10</th>
      <td>track</td>
      <td>BASE TABLE</td>
    </tr>
  </tbody>
</table>
</div>



### <font color=blue>03 Selecting Albums to Purchase</font>

#### <font color=blue>Primary Question...</font>

The Chinook record store has just signed a deal with a new record label, and you've been tasked with selecting the first three albums that will be added to the store, from a list of four. All four albums are by artists that don't have any tracks in the store right now - we have the artist names, and the genre of music they produce:

| Artist Name | Genre |
| :----- | :----- | 
|Regal| Hip-Hop | 
|Red Tone| Punk |
|Meteor and the Girls | pop |
|ASlim Jim Bites |Blues |

#### <font color=blue>Do the following to answer the question posed above</font>

-  <font color=black>Write a query that returns each genre, with the number of tracks sold in the united states in both absolute numbers and in percentages.  Here's a list strategic of steps taken to generate this query:</font>
-  <font color=black>Create a plot to show this data.</font>
-  <font color=black>Write a paragraph that interprets the data and makes a recommendation for the three artists whose albums we should purchase for the store, based on sales of tracks from their genres.  The table below</font>

 |


```python
query = '''
WITH usa_tracks_sold AS
   (
    SELECT il.* FROM invoice_line il
    INNER JOIN invoice i on il.invoice_id = i.invoice_id
    INNER JOIN customer c on i.customer_id = c.customer_id
    WHERE c.country = 'USA'
   )

SELECT
    g.name genre,
    count(uts.invoice_line_id) tracks_sold,
    cast(count(uts.invoice_line_id) AS FLOAT) / (
        SELECT COUNT(*) from usa_tracks_sold
    ) percentage_sold
FROM usa_tracks_sold uts
INNER JOIN track t on t.track_id = uts.track_id
INNER JOIN genre g on g.genre_id = t.genre_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
'''
albums_to_purchase = run_query(query)
# albums_to_purchase.set_index('genre')
albums_to_purchase

```




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
      <th>genre</th>
      <th>tracks_sold</th>
      <th>percentage_sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rock</td>
      <td>561</td>
      <td>0.533777</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alternative &amp; Punk</td>
      <td>130</td>
      <td>0.123692</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Metal</td>
      <td>124</td>
      <td>0.117983</td>
    </tr>
    <tr>
      <th>3</th>
      <td>R&amp;B/Soul</td>
      <td>53</td>
      <td>0.050428</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Blues</td>
      <td>36</td>
      <td>0.034253</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Alternative</td>
      <td>35</td>
      <td>0.033302</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Latin</td>
      <td>22</td>
      <td>0.020932</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Pop</td>
      <td>22</td>
      <td>0.020932</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Hip Hop/Rap</td>
      <td>20</td>
      <td>0.019029</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Jazz</td>
      <td>14</td>
      <td>0.013321</td>
    </tr>
  </tbody>
</table>
</div>




```python

albums_to_purchase.plot(kind='bar', x='genre', y='percentage_sold')
# x.show()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f3a441983c8>


