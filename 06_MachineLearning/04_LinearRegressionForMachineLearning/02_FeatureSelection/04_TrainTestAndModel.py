import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]
target = 'SalePrice'

# Selects/excludes columns based upon their dtypes. Super handy, I did this manually in the last chapter :(
numerical_train = train.select_dtypes(include=['int64', 'float64'])
# Drop the following columns that either have any missing values or need to be transformed to be useful
cols_to_drop = ['PID','Year Built','Year Remod/Add','Garage Yr Blt','Mo Sold','Yr Sold']
numerical_train = numerical_train.drop(cols_to_drop, axis=1)
# Create a Series object where the index is made up of column names and the associated values are the number of missing values
null_series = pd.Series(numerical_train.isnull().sum())
# keep only the columns with no missing values, and assign the resulting Series object to full_cols_series
full_cols_series = null_series[null_series==0]

# Determine the correlation of each feature column to the target column
train_subset = train[full_cols_series.index]
corrmat = train_subset.corr()
sorted_corrs = corrmat['SalePrice'].abs().sort_values()

# Limit the check to features with a correlation to the SalePrice >= 0.3
strong_corrs = sorted_corrs[sorted_corrs >= 0.3]

# Drop the columns that exhibit a strong Colinearity
final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])

# Check the data remaining dataset for missing values
# test[final_corr_cols.index].info()
# print('\n')

# The preceding check shows that Garage Area has a single missing value
# Since there's only only one that row will be dropped
clean_test = test[final_corr_cols.index].dropna(subset=['Garage Area']).copy()


# Build a linear regression model using the features in features.
# Calculate the RMSE on the test and train sets.
# Assign the train RMSE to train_rmse and the test RMSE to test_rmse.
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'
lr = LinearRegression()
lr.fit(train[features], train[target])

predict_train = lr.predict(train[features])
predict_test = lr.predict(clean_test[features])

train_mse = mean_squared_error(y_true=train[target], y_pred=predict_train)
train_rmse = np.sqrt(train_mse)
print('train_rmse:', train_rmse)
 
test_mse = mean_squared_error(y_true=clean_test[target], y_pred=predict_test)
test_rmse = np.sqrt(test_mse)
print('test_rmse:', test_rmse)
