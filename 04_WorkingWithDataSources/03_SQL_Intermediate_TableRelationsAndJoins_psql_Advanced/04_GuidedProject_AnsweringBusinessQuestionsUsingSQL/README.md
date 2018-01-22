
## <font color=blue>*chinook* DB Schema</font>
![chinook-schema](https://s3.amazonaws.com/dq-content/189/chinook-schema.svg)

### <font color=blue>02 Creating Helper Functions</font>
-  <font color=black>Import the psycopg2, pandas and matplotlib modules, and use the magic command <font color=red>*%matplotlib*</font> inline to make sure any plots render in the notebook.</font>
-  <font color=black>Create a <font color=red>*run_query()*</font> function, that takes a SQL query as an argument and returns a pandas dataframe of that query.</font>
-  <font color=black>Create a <font color=red>*run_command()*</font> function that takes a SQL command as an argument and executes it using the sqlite module.</font>
-  <font color=black>Create a <font color=red>*show_tables()*</font> function that calls the <font color=red>*run_query()*</font> function to return a list of all tables and views in the database.</font>
-  <font color=black>Run the <font color=red>*show_tables()*</font> function.</font>


```python
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
%matplotlib

conn = psycopg2.connect(dbname='chinook', user='kitestring', host="/tmp/", password='Chlorine35%')
cur = conn.cursor() 
```

    Using matplotlib backend: Qt5Agg



```python
def run_query(query):
    return pd.read_sql_query(query, conn)

def run_command(command):
    conn.execute(command)

def show_tables():
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
-  <font color=black>Write a query that returns each genre, with the number of tracks sold in absolute numbers and in percentages.</font>
-  <font color=black>Create a plot to show this data.</font>
-  <font color=black>Write a paragraph that interprets the data and makes a recommendation for the three artists whose albums we should purchase for the store, based on sales of tracks from their genres.</font>


```python
query = '''
SELECT
    COUNT(t.*) AS TotalTracks
FROM track t;
'''
genre_check = run_query(query)
genre_check
# conn.close()
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
      <th>totaltracks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3503</td>
    </tr>
  </tbody>
</table>
</div>


