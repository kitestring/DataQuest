
# coding: utf-8

# In[163]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## <font color=blue>01 Introduction to the data set</font> 
# *  Read __imports-85.data__ ([data set description](https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names)) into a dataframe named __cars__. If you read in the file using [pandas.read_csv()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) without specifying any additional parameter values, you'll notice that the column names don't match the ones in the [dataset's documentation](https://archive.ics.uci.edu/ml/datasets/automobile). Why do you think this is and how can you fix this?
# *  Determine which columns are numeric and can be used as features and which column is the target column.
# *  Display the first few rows of the dataframe and make sure it looks like the data set preview.

# In[164]:


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


# ## <font color=blue>02 Data Cleaning</font>
# *  Use the [DataFrame.replace()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html) method to replace all of the __?__ values with the __numpy.nan__ missing value.
# *  Because __?__ is a string value, columns containing this value were cast to the pandas __object__ data type (instead of a numeric type like __int__ or __float__). After replacing the ? values, determine which columns need to be converted to numeric types. You can use either the [DataFrame.astype()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.astype.html) or the [Series.astype()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.astype.html) methods to convert column types.
# *  Return the number of rows that have a missing value for the __normalized-losses__ column. Determine how you should handle this column. You could:
#   *  Replace the missing values using the average values from that column.
#   *  Drop the rows entirely (especially if other columns in those rows have missing values).
#   *  Drop the column entirely.
# *  Explore the missing value counts for the other numeric columns and handle any missing values.
# *  Of the columns you decided to keep, normalize the numeric ones so all values range from __0__ to __1__.

# In[165]:


print('Convert missing values (?) with np.NaN then set the type to float')
numeric_cars.replace(to_replace='?', value=np.nan, inplace=True)
numeric_cars = numeric_cars.astype('float')
print(numeric_cars.info())
numeric_cars.head(10)


# In[166]:


print('This shows the percentage of values in each column that are not numberic.')

not_numeric_count = len(numeric_cars) - numeric_cars.count(axis=0, level=None, numeric_only=False)
percentage_not_numeric = (not_numeric_count / len(numeric_cars)) * 100
percentage_not_numeric


# In[167]:


print("Because the column we're trying to predict is 'price', any row were price is NaN will be removed.")
print("After doings so we will again check the percentage of values that are NaN for each column")
numeric_cars.dropna(subset=['price'], inplace=True)
not_numeric_count = len(numeric_cars) - numeric_cars.count(axis=0, level=None, numeric_only=False)
percentage_not_numeric = (not_numeric_count / len(numeric_cars)) * 100
percentage_not_numeric


# In[168]:


print("All remaining NaN's will be filled with the mean of its respective column")
numeric_cars = numeric_cars.fillna(numeric_cars.mean())
print("Then, verify that all NaN's have been removed by showing the number of NaN's for each column.\n")
numeric_cars.isnull().sum()


# In[169]:


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


# ## <font color=blue>03 Univariate Model</font>
# *  Create a function, named __knn_train_test()__ that encapsulates the training and simple validation process. This function should have 3 parameters -- training column name, target column name, and the dataframe object.
#   *  This function should split the data set into a training and test set.
#   *  Then, it should instantiate the KNeighborsRegressor class, fit the model on the training set, and make predictions on the test set.
#   *  Finally, it should calculate the RMSE and return that value.
# *  Use this function to train and test univariate models using the different numeric columns in the data set. Which column performed the best using the default __k__ value?
# *  Modify the __knn_train_test()__ function you wrote to accept a parameter for the __k__ value.
#   *  Update the function logic to use this parameter.
#   *  For each numeric column, create, train, and test a univariate model using the following __k__ values (__1__, __3__, __5__, __7__, and __9__). Visualize the results using a scatter plot and a line plot.

# In[170]:


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


# In[171]:


# instantiate mse dict
mse_dict = {}

for feature in test_features:
    print(feature)
    # instantiate mse list
    mse = [knn_train_test(df=numeric_cars_normalized, train_features=feature, predict_feature=predictive_feature, k_value=k) for k in k_values]
    mse_dict[feature] = mse
    
mse_dict


# ## <font color=blue>04 Mulitvariate Model</font>
# *  Modify the __knn_train_test()__ function to accept a list of column names (instead of just a string). Modify the rest of the function logic to use this parameter:
#   *  Instead of using just a single column for train and test, use all of the columns passed in.
#   *  Use a the default k value from scikit-learn for now (we'll tune the k value in the next step).
# *  Use the best 2 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
# *  Use the best 3 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
# *  Use the best 4 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
# *  Use the best 5 features from the previous step to train and test a multivariate k-nearest neighbors model using the default __k__ value.
# *  Display all of the RMSE values.

# ## <font color=blue>05 Hyperparameter Tuning</font>
# *  For the top 3 models in the last step, vary the hyperparameter value from __1__ to __25__ and plot the resulting RMSE values.
# *  Which __k__ value is optimal for each model? How different are the __k__ values and what do you think accounts for the differences?
