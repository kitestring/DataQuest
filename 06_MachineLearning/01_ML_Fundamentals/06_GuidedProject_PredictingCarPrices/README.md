

```python
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## <font color=blue>01 Introduction to the data set</font> 
*  Read __imports-85.data__ ([data set description](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names)) into a dataframe named __cars__. If you read in the file using [pandas.read_csv()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) without specifying any additional parameter values, you'll notice that the column names don't match the ones in the [dataset's documentation](https://archive.ics.uci.edu/ml/datasets/automobile). Why do you think this is and how can you fix this?
*  Determine which columns are numeric and can be used as features and which column is the target column.
*  Display the first few rows of the dataframe and make sure it looks like the data set preview.


```python
headers=['symboling','normalized_losses','make','fuel_type','aspiration','num_of_doors',
         'body_style','drive_wheels','engine_location','wheel_base','length','width',
        'height','curb_weight','engine_type','num_of_cylinders','engine_size','fuel_system',
        'bore','stroke','compression_ratio','horsepower','peak_rpm','city_mpg','highway_mpg',
        'price']
cars = pd.read_csv('imports-85.data.txt', names=headers)

# Select only the columns with continuous values from - https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names
continuous_values_cols = ['normalized_losses', 'wheel_base', 'length', 'width', 'height', 'curb_weight', 'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm', 'city_mpg', 'highway_mpg', 'price']
numeric_cars = cars[continuous_values_cols].copy()
print(numeric_cars.info())
numeric_cars.head(10)
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 205 entries, 0 to 204
    Data columns (total 14 columns):
    normalized_losses    205 non-null object
    wheel_base           205 non-null float64
    length               205 non-null float64
    width                205 non-null float64
    height               205 non-null float64
    curb_weight          205 non-null int64
    bore                 205 non-null object
    stroke               205 non-null object
    compression_ratio    205 non-null float64
    horsepower           205 non-null object
    peak_rpm             205 non-null object
    city_mpg             205 non-null int64
    highway_mpg          205 non-null int64
    price                205 non-null object
    dtypes: float64(5), int64(3), object(6)
    memory usage: 22.5+ KB
    None





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
      <th>normalized_losses</th>
      <th>wheel_base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb_weight</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression_ratio</th>
      <th>horsepower</th>
      <th>peak_rpm</th>
      <th>city_mpg</th>
      <th>highway_mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>?</td>
      <td>88.6</td>
      <td>168.8</td>
      <td>64.1</td>
      <td>48.8</td>
      <td>2548</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>13495</td>
    </tr>
    <tr>
      <th>1</th>
      <td>?</td>
      <td>88.6</td>
      <td>168.8</td>
      <td>64.1</td>
      <td>48.8</td>
      <td>2548</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>?</td>
      <td>94.5</td>
      <td>171.2</td>
      <td>65.5</td>
      <td>52.4</td>
      <td>2823</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.0</td>
      <td>154</td>
      <td>5000</td>
      <td>19</td>
      <td>26</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>164</td>
      <td>99.8</td>
      <td>176.6</td>
      <td>66.2</td>
      <td>54.3</td>
      <td>2337</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>13950</td>
    </tr>
    <tr>
      <th>4</th>
      <td>164</td>
      <td>99.4</td>
      <td>176.6</td>
      <td>66.4</td>
      <td>54.3</td>
      <td>2824</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115</td>
      <td>5500</td>
      <td>18</td>
      <td>22</td>
      <td>17450</td>
    </tr>
    <tr>
      <th>5</th>
      <td>?</td>
      <td>99.8</td>
      <td>177.3</td>
      <td>66.3</td>
      <td>53.1</td>
      <td>2507</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>15250</td>
    </tr>
    <tr>
      <th>6</th>
      <td>158</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.7</td>
      <td>2844</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>17710</td>
    </tr>
    <tr>
      <th>7</th>
      <td>?</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.7</td>
      <td>2954</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>18920</td>
    </tr>
    <tr>
      <th>8</th>
      <td>158</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.9</td>
      <td>3086</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>8.3</td>
      <td>140</td>
      <td>5500</td>
      <td>17</td>
      <td>20</td>
      <td>23875</td>
    </tr>
    <tr>
      <th>9</th>
      <td>?</td>
      <td>99.5</td>
      <td>178.2</td>
      <td>67.9</td>
      <td>52.0</td>
      <td>3053</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>7.0</td>
      <td>160</td>
      <td>5500</td>
      <td>16</td>
      <td>22</td>
      <td>?</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>02 Data Cleaning</font>
*  Use the [DataFrame.replace()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html) method to replace all of the __?__ values with the __numpy.nan__ missing value.
*  Because __?__ is a string value, columns containing this value were cast to the pandas __object__ data type (instead of a numeric type like __int__ or __float__). After replacing the ? values, determine which columns need to be converted to numeric types. You can use either the [DataFrame.astype()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.astype.html) or the [Series.astype()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.astype.html) methods to convert column types.
*  Return the number of rows that have a missing value for the __normalized-losses__ column. Determine how you should handle this column. You could:
  *  Replace the missing values using the average values from that column.
  *  Drop the rows entirely (especially if other columns in those rows have missing values).
  *  Drop the column entirely.
*  Explore the missing value counts for the other numeric columns and handle any missing values.
*  Of the columns you decided to keep, normalize the numeric ones so all values range from __0__ to __1__.


```python
print('Convert missing values (?) with np.NaN then set the type to float')
numeric_cars.replace(to_replace='?', value=np.nan, inplace=True)
numeric_cars = numeric_cars.astype('float')
print(numeric_cars.info())
numeric_cars.head(10)
```

    Convert missing values (?) with np.NaN then set the type to float
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 205 entries, 0 to 204
    Data columns (total 14 columns):
    normalized_losses    164 non-null float64
    wheel_base           205 non-null float64
    length               205 non-null float64
    width                205 non-null float64
    height               205 non-null float64
    curb_weight          205 non-null float64
    bore                 201 non-null float64
    stroke               201 non-null float64
    compression_ratio    205 non-null float64
    horsepower           203 non-null float64
    peak_rpm             203 non-null float64
    city_mpg             205 non-null float64
    highway_mpg          205 non-null float64
    price                201 non-null float64
    dtypes: float64(14)
    memory usage: 22.5 KB
    None





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
      <th>normalized_losses</th>
      <th>wheel_base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb_weight</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression_ratio</th>
      <th>horsepower</th>
      <th>peak_rpm</th>
      <th>city_mpg</th>
      <th>highway_mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>88.6</td>
      <td>168.8</td>
      <td>64.1</td>
      <td>48.8</td>
      <td>2548.0</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111.0</td>
      <td>5000.0</td>
      <td>21.0</td>
      <td>27.0</td>
      <td>13495.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>88.6</td>
      <td>168.8</td>
      <td>64.1</td>
      <td>48.8</td>
      <td>2548.0</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111.0</td>
      <td>5000.0</td>
      <td>21.0</td>
      <td>27.0</td>
      <td>16500.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>94.5</td>
      <td>171.2</td>
      <td>65.5</td>
      <td>52.4</td>
      <td>2823.0</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.0</td>
      <td>154.0</td>
      <td>5000.0</td>
      <td>19.0</td>
      <td>26.0</td>
      <td>16500.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>164.0</td>
      <td>99.8</td>
      <td>176.6</td>
      <td>66.2</td>
      <td>54.3</td>
      <td>2337.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102.0</td>
      <td>5500.0</td>
      <td>24.0</td>
      <td>30.0</td>
      <td>13950.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>164.0</td>
      <td>99.4</td>
      <td>176.6</td>
      <td>66.4</td>
      <td>54.3</td>
      <td>2824.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115.0</td>
      <td>5500.0</td>
      <td>18.0</td>
      <td>22.0</td>
      <td>17450.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>99.8</td>
      <td>177.3</td>
      <td>66.3</td>
      <td>53.1</td>
      <td>2507.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110.0</td>
      <td>5500.0</td>
      <td>19.0</td>
      <td>25.0</td>
      <td>15250.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>158.0</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.7</td>
      <td>2844.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110.0</td>
      <td>5500.0</td>
      <td>19.0</td>
      <td>25.0</td>
      <td>17710.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.7</td>
      <td>2954.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110.0</td>
      <td>5500.0</td>
      <td>19.0</td>
      <td>25.0</td>
      <td>18920.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>158.0</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.9</td>
      <td>3086.0</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>8.3</td>
      <td>140.0</td>
      <td>5500.0</td>
      <td>17.0</td>
      <td>20.0</td>
      <td>23875.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>99.5</td>
      <td>178.2</td>
      <td>67.9</td>
      <td>52.0</td>
      <td>3053.0</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>7.0</td>
      <td>160.0</td>
      <td>5500.0</td>
      <td>16.0</td>
      <td>22.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('This shows the percentage of values in each column that are not numberic.')

not_numeric_count = len(numeric_cars) - numeric_cars.count(axis=0, level=None, numeric_only=False)
percentage_not_numeric = (not_numeric_count / len(numeric_cars)) * 100
percentage_not_numeric
```

    This shows the percentage of values in each column that are not numberic.





    normalized_losses    20.00000
    wheel_base            0.00000
    length                0.00000
    width                 0.00000
    height                0.00000
    curb_weight           0.00000
    bore                  1.95122
    stroke                1.95122
    compression_ratio     0.00000
    horsepower            0.97561
    peak_rpm              0.97561
    city_mpg              0.00000
    highway_mpg           0.00000
    price                 1.95122
    dtype: float64




```python
print("Because the column we're trying to predict is 'price', any row were price is NaN will be removed.")
print("After doings so we will again check the percentage of values that are NaN for each column")
numeric_cars.dropna(subset=['price'], inplace=True)
not_numeric_count = len(numeric_cars) - numeric_cars.count(axis=0, level=None, numeric_only=False)
percentage_not_numeric = (not_numeric_count / len(numeric_cars)) * 100
percentage_not_numeric
```

    Because the column we're trying to predict is 'price', any row were price is NaN will be removed.
    After doings so we will again check the percentage of values that are NaN for each column





    normalized_losses    18.407960
    wheel_base            0.000000
    length                0.000000
    width                 0.000000
    height                0.000000
    curb_weight           0.000000
    bore                  1.990050
    stroke                1.990050
    compression_ratio     0.000000
    horsepower            0.995025
    peak_rpm              0.995025
    city_mpg              0.000000
    highway_mpg           0.000000
    price                 0.000000
    dtype: float64




```python
print("All remaining NaN's will be filled with the mean of its respective column")
numeric_cars = numeric_cars.fillna(numeric_cars.mean())
print("Then, verify that all NaN's have been removed by showing the number of NaN's for each column.\n")
numeric_cars.isnull().sum()
```

    All remaining NaN's will be filled with the mean of its respective column
    Then, verify that all NaN's have been removed by showing the number of NaN's for each column.
    





    normalized_losses    0
    wheel_base           0
    length               0
    width                0
    height               0
    curb_weight          0
    bore                 0
    stroke               0
    compression_ratio    0
    horsepower           0
    peak_rpm             0
    city_mpg             0
    highway_mpg          0
    price                0
    dtype: int64




```python
# Create training feature list and k value list
test_features = numeric_cars.columns.tolist()
predictive_feature = 'price'
test_features.remove(predictive_feature)
k_values = [x for x in range(10) if x/2 != round(x/2)]

# Normalize columns
numeric_cars_normalized = numeric_cars[test_features].copy()
numeric_cars_normalized = numeric_cars_normalized/ numeric_cars.max()
numeric_cars_normalized[predictive_feature] = numeric_cars[predictive_feature].copy()
numeric_cars_normalized.head(5)
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
      <th>bore</th>
      <th>city_mpg</th>
      <th>compression_ratio</th>
      <th>curb_weight</th>
      <th>height</th>
      <th>highway_mpg</th>
      <th>horsepower</th>
      <th>length</th>
      <th>normalized_losses</th>
      <th>peak_rpm</th>
      <th>price</th>
      <th>stroke</th>
      <th>wheel_base</th>
      <th>width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.880711</td>
      <td>0.428571</td>
      <td>0.391304</td>
      <td>0.626660</td>
      <td>0.816054</td>
      <td>0.500000</td>
      <td>0.423664</td>
      <td>0.811148</td>
      <td>0.476562</td>
      <td>0.757576</td>
      <td>13495.0</td>
      <td>0.642686</td>
      <td>0.732837</td>
      <td>0.890278</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.880711</td>
      <td>0.428571</td>
      <td>0.391304</td>
      <td>0.626660</td>
      <td>0.816054</td>
      <td>0.500000</td>
      <td>0.423664</td>
      <td>0.811148</td>
      <td>0.476562</td>
      <td>0.757576</td>
      <td>16500.0</td>
      <td>0.642686</td>
      <td>0.732837</td>
      <td>0.890278</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.680203</td>
      <td>0.387755</td>
      <td>0.391304</td>
      <td>0.694294</td>
      <td>0.876254</td>
      <td>0.481481</td>
      <td>0.587786</td>
      <td>0.822681</td>
      <td>0.476562</td>
      <td>0.757576</td>
      <td>16500.0</td>
      <td>0.832134</td>
      <td>0.781638</td>
      <td>0.909722</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.809645</td>
      <td>0.489796</td>
      <td>0.434783</td>
      <td>0.574766</td>
      <td>0.908027</td>
      <td>0.555556</td>
      <td>0.389313</td>
      <td>0.848630</td>
      <td>0.640625</td>
      <td>0.833333</td>
      <td>13950.0</td>
      <td>0.815348</td>
      <td>0.825476</td>
      <td>0.919444</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.809645</td>
      <td>0.367347</td>
      <td>0.347826</td>
      <td>0.694540</td>
      <td>0.908027</td>
      <td>0.407407</td>
      <td>0.438931</td>
      <td>0.848630</td>
      <td>0.640625</td>
      <td>0.833333</td>
      <td>17450.0</td>
      <td>0.815348</td>
      <td>0.822167</td>
      <td>0.922222</td>
    </tr>
  </tbody>
</table>
</div>



## <font color=blue>03 Univariate Model</font>
*  Create a function, named __knn_train_test()__ that encapsulates the training and simple validation process. This function should have 3 parameters -- training column name, target column name, and the dataframe object.
  *  This function should split the data set into a training and test set.
  *  Then, it should instantiate the KNeighborsRegressor class, fit the model on the training set, and make predictions on the test set.
  *  Finally, it should calculate the RMSE and return that value.
*  Use this function to train and test univariate models using the different numeric columns in the data set. Which column performed the best using the default __k__ value?
*  Modify the __knn_train_test()__ function you wrote to accept a parameter for the __k__ value.
  *  Update the function logic to use this parameter.
  *  For each numeric column, create, train, and test a univariate model using the following __k__ values (__1__, __3__, __5__, __7__, and __9__). Visualize the results using a scatter plot and a line plot.


```python
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def knn_train_test(df, train_features, predict_feature, k_value):
    # Randomly resorts the DataFrame to mitiate sampling bias
    np.random.seed(1)
    df = df.loc[np.random.permutation(len(numeric_cars))]

    # Split the DataFrame into ~75% train / 25% test data sets
    split_integer = round(len(df) * 0.75)
    train_df = df.iloc[0:split_integer]
    test_df = df.iloc[split_integer:]
    
    # Trains the model
    knn = KNeighborsRegressor(n_neighbors=k_value)
    knn.fit(train_df[[train_features]], train_df[predict_feature])
    
    # Test the model & return calculate mean square error
    predictions = knn.predict(test_df[train_features])
    print("predictions")
    mse = mean_squared_error(y_true=test_df[predict_feature], y_pred=predictions)
    return mse
```


```python
# instantiate mse dict
mse_dict = {}

for feature in test_features:
    print(feature)
    # instantiate mse list
    mse = [knn_train_test(df=numeric_cars_normalized, train_features=feature, predict_feature=predictive_feature, k_value=k) for k in k_values]
    mse_dict[feature] = mse
    
mse_dict
```

    normalized_losses



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-171-edf06703e8b1> in <module>()
          5     print(feature)
          6     # instantiate mse list
    ----> 7     mse = [knn_train_test(df=numeric_cars_normalized, train_features=feature, predict_feature=predictive_feature, k_value=k) for k in k_values]
          8     mse_dict[feature] = mse
          9 


    <ipython-input-171-edf06703e8b1> in <listcomp>(.0)
          5     print(feature)
          6     # instantiate mse list
    ----> 7     mse = [knn_train_test(df=numeric_cars_normalized, train_features=feature, predict_feature=predictive_feature, k_value=k) for k in k_values]
          8     mse_dict[feature] = mse
          9 


    <ipython-input-170-4214cc777bb6> in knn_train_test(df, train_features, predict_feature, k_value)
         14     # Trains the model
         15     knn = KNeighborsRegressor(n_neighbors=k_value)
    ---> 16     knn.fit(train_df[[train_features]], train_df[predict_feature])
         17 
         18     # Test the model & return calculate mean square error


    ~/anaconda3/lib/python3.6/site-packages/sklearn/neighbors/base.py in fit(self, X, y)
        743         """
        744         if not isinstance(X, (KDTree, BallTree)):
    --> 745             X, y = check_X_y(X, y, "csr", multi_output=True)
        746         self._y = y
        747         return self._fit(X)


    ~/anaconda3/lib/python3.6/site-packages/sklearn/utils/validation.py in check_X_y(X, y, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, warn_on_dtype, estimator)
        540     X = check_array(X, accept_sparse, dtype, order, copy, force_all_finite,
        541                     ensure_2d, allow_nd, ensure_min_samples,
    --> 542                     ensure_min_features, warn_on_dtype, estimator)
        543     if multi_output:
        544         y = check_array(y, 'csr', force_all_finite=True, ensure_2d=False,


    ~/anaconda3/lib/python3.6/site-packages/sklearn/utils/validation.py in check_array(array, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, warn_on_dtype, estimator)
        420                              % (array.ndim, estimator_name))
        421         if force_all_finite:
    --> 422             _assert_all_finite(array)
        423 
        424     shape_repr = _shape_repr(array.shape)


    ~/anaconda3/lib/python3.6/site-packages/sklearn/utils/validation.py in _assert_all_finite(X)
         41             and not np.isfinite(X).all()):
         42         raise ValueError("Input contains NaN, infinity"
    ---> 43                          " or a value too large for %r." % X.dtype)
         44 
         45 


    ValueError: Input contains NaN, infinity or a value too large for dtype('float64').


## <font color=blue>04 Mulitvariate Model</font>
*  Modify the __knn_train_test()__ function to accept a list of column names (instead of just a string). Modify the rest of the function logic to use this parameter:
  *  Instead of using just a single column for train and test, use all of the columns passed in.
  *  Use a the default k value from scikit-learn for now (we'll tune the k value in the next step).
*  Use the best 2 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
*  Use the best 3 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
*  Use the best 4 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
*  Use the best 5 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
*  Display all of the RMSE values.

## <font color=blue>05 Hyperparameter Tuning</font>
*  For the top 3 models in the last step, vary the hyperparameter value from __1__ to __25__ and plot the resulting RMSE values.
*  Which __k__ value is optimal for each model? How different are the __k__ values and what do you think accounts for the differences?
