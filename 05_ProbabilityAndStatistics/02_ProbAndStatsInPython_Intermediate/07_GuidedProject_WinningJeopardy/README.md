
## <font color=blue>01 Jeopardy Questions</font>
*  Read the dataset into a Dataframe called __jeopardy__ using Pandas.
*  Print out the first __5__ rows of __jeopardy__.
*  Print out the columns of __jeopardy__ using __jeopardy.columns__.
*  Some of the column names have spaces in front.
  *  Remove the spaces in each item in __jeopardy.columns__.
  *  Assign the result back to __jeopardy.columns__ to fix the column names in __jeopardy__.
*  Make sure you pay close attention to the format of each column.


```python
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from scipy.stats import pearsonr
# from scipy.stats import linregress
```


```python
jeopardy = pd.read_csv('JEOPARDY_CSV.csv')
jeopardy.rename(columns=lambda col_header: col_header.strip(), inplace=True)
print('Column Header dtypes\n')
print(jeopardy.dtypes)
jeopardy.head(10)
```

    Column Header dtypes
    
    Show Number     int64
    Air Date       object
    Round          object
    Category       object
    Value          object
    Question       object
    Answer         object
    dtype: object





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
      <th>Show Number</th>
      <th>Air Date</th>
      <th>Round</th>
      <th>Category</th>
      <th>Value</th>
      <th>Question</th>
      <th>Answer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>HISTORY</td>
      <td>$200</td>
      <td>For the last 8 years of his life, Galileo was ...</td>
      <td>Copernicus</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>ESPN's TOP 10 ALL-TIME ATHLETES</td>
      <td>$200</td>
      <td>No. 2: 1912 Olympian; football star at Carlisl...</td>
      <td>Jim Thorpe</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>EVERYBODY TALKS ABOUT IT...</td>
      <td>$200</td>
      <td>The city of Yuma in this state has a record av...</td>
      <td>Arizona</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>THE COMPANY LINE</td>
      <td>$200</td>
      <td>In 1963, live on "The Art Linkletter Show", th...</td>
      <td>McDonald's</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>EPITAPHS &amp; TRIBUTES</td>
      <td>$200</td>
      <td>Signer of the Dec. of Indep., framer of the Co...</td>
      <td>John Adams</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>3-LETTER WORDS</td>
      <td>$200</td>
      <td>In the title of an Aesop fable, this insect sh...</td>
      <td>the ant</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>HISTORY</td>
      <td>$400</td>
      <td>Built in 312 B.C. to link Rome &amp; the South of ...</td>
      <td>the Appian Way</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>ESPN's TOP 10 ALL-TIME ATHLETES</td>
      <td>$400</td>
      <td>No. 8: 30 steals for the Birmingham Barons; 2,...</td>
      <td>Michael Jordan</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>EVERYBODY TALKS ABOUT IT...</td>
      <td>$400</td>
      <td>In the winter of 1971-72, a record 1,122 inche...</td>
      <td>Washington</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4680</td>
      <td>2004-12-31</td>
      <td>Jeopardy!</td>
      <td>THE COMPANY LINE</td>
      <td>$400</td>
      <td>This housewares store was named for the packag...</td>
      <td>Crate &amp; Barrel</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>02 Normalizing Text</font>
*  Write a function to normalize questions and answers. It should:
  *  Take in a string.
  *  Convert the string to lowercase.
  *  Remove all punctuation in the string.
  *  Return the string.
*  Normalize the __Question__ column.
  *  Use the Pandas apply method to apply the function to each item in the __Question__ column.
  *  Assign the result to the __clean_question__ column.
*  Normalize the __Answer__ column.
  *  Use the Pandas apply method to apply the function to each item in the __Answer__ column. 
  *  Assign the result to the __clean_answer__ column.


```python
import string

def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation)
    return  s.translate(translator)

def normalize_string_column(row, col_name):
    # removes all punctuation from a string and converts to lower case
    no_punctuation = remove_punctuation(row[col_name])
    return no_punctuation.lower()

cols_to_normalize_columns = ['Question', 'Answer']
normalized_columns = ['clean_question', 'clean_answer']

for i in range(len(cols_to_normalize_columns)):
    jeopardy[normalized_columns[i]] = jeopardy.apply(normalize_string_column, args=(cols_to_normalize_columns[i],), axis=1)
    
jeopardy.tail(10)
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
      <th>Show Number</th>
      <th>Air Date</th>
      <th>Round</th>
      <th>Category</th>
      <th>Value</th>
      <th>Question</th>
      <th>Answer</th>
      <th>clean_question</th>
      <th>clean_answer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>216920</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>"T" BIRDS</td>
      <td>$1600</td>
      <td>Nightingales &amp; robins belong to this family of...</td>
      <td>thrushes</td>
      <td>nightingales  robins belong to this family of ...</td>
      <td>thrushes</td>
    </tr>
    <tr>
      <th>216921</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>AUTHORS IN THEIR YOUTH</td>
      <td>$1600</td>
      <td>Her hotsy-totsy diaries trace back to one she ...</td>
      <td>Anaïs Nin</td>
      <td>her hotsytotsy diaries trace back to one she b...</td>
      <td>anaïs nin</td>
    </tr>
    <tr>
      <th>216922</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>QUOTATIONS</td>
      <td>$1600</td>
      <td>A motto of hers was "in politics, if you want ...</td>
      <td>(Margaret) Thatcher</td>
      <td>a motto of hers was in politics if you want an...</td>
      <td>margaret thatcher</td>
    </tr>
    <tr>
      <th>216923</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>WORLD CAPITALS</td>
      <td>$2000</td>
      <td>It's on the Suriname River</td>
      <td>Paramaribo</td>
      <td>its on the suriname river</td>
      <td>paramaribo</td>
    </tr>
    <tr>
      <th>216924</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>OFF-BROADWAY</td>
      <td>$2000</td>
      <td>In 2006 the cast of this long-running hit emba...</td>
      <td>Stomp</td>
      <td>in 2006 the cast of this longrunning hit embar...</td>
      <td>stomp</td>
    </tr>
    <tr>
      <th>216925</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>RIDDLE ME THIS</td>
      <td>$2000</td>
      <td>This Puccini opera turns on the solution to 3 ...</td>
      <td>Turandot</td>
      <td>this puccini opera turns on the solution to 3 ...</td>
      <td>turandot</td>
    </tr>
    <tr>
      <th>216926</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>"T" BIRDS</td>
      <td>$2000</td>
      <td>In North America this term is properly applied...</td>
      <td>a titmouse</td>
      <td>in north america this term is properly applied...</td>
      <td>a titmouse</td>
    </tr>
    <tr>
      <th>216927</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>AUTHORS IN THEIR YOUTH</td>
      <td>$2000</td>
      <td>In Penny Lane, where this "Hellraiser" grew up...</td>
      <td>Clive Barker</td>
      <td>in penny lane where this hellraiser grew up th...</td>
      <td>clive barker</td>
    </tr>
    <tr>
      <th>216928</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>QUOTATIONS</td>
      <td>$2000</td>
      <td>From Ft. Sill, Okla. he made the plea, Arizona...</td>
      <td>Geronimo</td>
      <td>from ft sill okla he made the plea arizona is ...</td>
      <td>geronimo</td>
    </tr>
    <tr>
      <th>216929</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Final Jeopardy!</td>
      <td>HISTORIC NAMES</td>
      <td>None</td>
      <td>A silent movie title includes the last name of...</td>
      <td>Grigori Alexandrovich Potemkin</td>
      <td>a silent movie title includes the last name of...</td>
      <td>grigori alexandrovich potemkin</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>03 Normalizing Columns</font>
*  Write a function to normalize dollar values. It should:
  *  Take in a string.
  *  Remove any punctuation in the string.
  *  Convert the string to an integer.
  *  If the conversion has an error, assign __0__ instead.
  *  Return the integer.
*  Normalize the __Value__ column.
  *  Use the Pandas apply method to apply the function to each item in the __Value__ column.
  *  Assign the result to the __clean_value__ column.
*  Use the [pandas.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) function to convert the __Air Date__ column to a datetime column.


```python
def normalize_dollar_values(row, col_name):
    no_punctuation = remove_punctuation(row[col_name])
    try:
        return int(no_punctuation)
    except ValueError:
        return 0

jeopardy['clean_value'] = jeopardy.apply(normalize_dollar_values, args=('Value',), axis=1)
jeopardy['Air Date'] = pd.to_datetime(jeopardy['Air Date'], format='%Y-%m-%d', errors='raise')

print('Column Header dtypes\n')
print(jeopardy.dtypes)
jeopardy.tail(10)
```

    Column Header dtypes
    
    Show Number                int64
    Air Date          datetime64[ns]
    Round                     object
    Category                  object
    Value                     object
    Question                  object
    Answer                    object
    clean_question            object
    clean_answer              object
    clean_value                int64
    dtype: object





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
      <th>Show Number</th>
      <th>Air Date</th>
      <th>Round</th>
      <th>Category</th>
      <th>Value</th>
      <th>Question</th>
      <th>Answer</th>
      <th>clean_question</th>
      <th>clean_answer</th>
      <th>clean_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>216920</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>"T" BIRDS</td>
      <td>$1600</td>
      <td>Nightingales &amp; robins belong to this family of...</td>
      <td>thrushes</td>
      <td>nightingales  robins belong to this family of ...</td>
      <td>thrushes</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>216921</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>AUTHORS IN THEIR YOUTH</td>
      <td>$1600</td>
      <td>Her hotsy-totsy diaries trace back to one she ...</td>
      <td>Anaïs Nin</td>
      <td>her hotsytotsy diaries trace back to one she b...</td>
      <td>anaïs nin</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>216922</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>QUOTATIONS</td>
      <td>$1600</td>
      <td>A motto of hers was "in politics, if you want ...</td>
      <td>(Margaret) Thatcher</td>
      <td>a motto of hers was in politics if you want an...</td>
      <td>margaret thatcher</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>216923</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>WORLD CAPITALS</td>
      <td>$2000</td>
      <td>It's on the Suriname River</td>
      <td>Paramaribo</td>
      <td>its on the suriname river</td>
      <td>paramaribo</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>216924</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>OFF-BROADWAY</td>
      <td>$2000</td>
      <td>In 2006 the cast of this long-running hit emba...</td>
      <td>Stomp</td>
      <td>in 2006 the cast of this longrunning hit embar...</td>
      <td>stomp</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>216925</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>RIDDLE ME THIS</td>
      <td>$2000</td>
      <td>This Puccini opera turns on the solution to 3 ...</td>
      <td>Turandot</td>
      <td>this puccini opera turns on the solution to 3 ...</td>
      <td>turandot</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>216926</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>"T" BIRDS</td>
      <td>$2000</td>
      <td>In North America this term is properly applied...</td>
      <td>a titmouse</td>
      <td>in north america this term is properly applied...</td>
      <td>a titmouse</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>216927</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>AUTHORS IN THEIR YOUTH</td>
      <td>$2000</td>
      <td>In Penny Lane, where this "Hellraiser" grew up...</td>
      <td>Clive Barker</td>
      <td>in penny lane where this hellraiser grew up th...</td>
      <td>clive barker</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>216928</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Double Jeopardy!</td>
      <td>QUOTATIONS</td>
      <td>$2000</td>
      <td>From Ft. Sill, Okla. he made the plea, Arizona...</td>
      <td>Geronimo</td>
      <td>from ft sill okla he made the plea arizona is ...</td>
      <td>geronimo</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>216929</th>
      <td>4999</td>
      <td>2006-05-11</td>
      <td>Final Jeopardy!</td>
      <td>HISTORIC NAMES</td>
      <td>None</td>
      <td>A silent movie title includes the last name of...</td>
      <td>Grigori Alexandrovich Potemkin</td>
      <td>a silent movie title includes the last name of...</td>
      <td>grigori alexandrovich potemkin</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>04 Answers in Questions</font>
*  Write a function that takes in a row in __jeopardy__, as a Series. It should:
  *  Split the __clean_answer__ column on the space character (), and assign to the variable __split_answer__.
    *  Split the __clean_question__ column on the space character (), and assign to the variable __split_question__.
  *  Create a variable called __match_count__, and set it to __0__.
  *  If the is in split_answer, remove it using the remove method on lists. The is commonly found in answers and questions, but doesn't have any meaningful use in finding the answer.
  *  If __the__ length of split_answer is __0__, return __0__. This prevents a division by zero error later.
  *  Loop through each item in __split_answer__, and see if it occurs in __split_question__. If it does, add __1__ to __match_count__.
  *  Divide __match_count__ by the length of __split_answer__, and return the result.
*  Count how many times terms in __clean_answer__ occur in __clean_question__.
  *  Use the Pandas [apply](http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.apply.html) method on Dataframes to apply the function to each row in __jeopardy__.
  *  Pass the __axis=1__ argument to apply the function across each row.
  *  Assign the result to the __answer_in_question__ column.
*  Find the mean of the __answer_in_question__ column using the [mean](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.mean.html) method on Series.
*  Write up a markdown cell with a short explanation of how finding this mean might influence your studying strategy for Jeopardy.
