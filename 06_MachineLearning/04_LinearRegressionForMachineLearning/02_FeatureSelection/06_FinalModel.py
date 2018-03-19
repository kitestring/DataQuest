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

# The preceding check shows that Garage Area has a single missing value
# Since there's only only one that row will be dropped
clean_test = test[final_corr_cols.index].dropna(subset=['Garage Area']).copy()

# The final cleaning step is to remove features with variance > 0.015
features  = ['Wood Deck SF', 'Fireplaces', 'Full Bath',
       '1st Flr SF', 'Garage Area', 'Gr Liv Area', 'Overall Qual']

target = 'SalePrice'

# Build a linear regression model using the remaining features.
# Calculate the RMSE on the test and train sets.
# Assign the train RMSE to train_rmse_2 and the test RMSE to test_rmse_2.

lr = LinearRegression()

lr.fit(train[features], train[target])
train_predict_2 = lr.predict(train[features])
test_predict_2 = lr.predict(clean_test[features])

train_mse_2 = mean_squared_error(y_true=train[target], y_pred=train_predict_2)
test_mse_2 = mean_squared_error(y_true=clean_test[target], y_pred=test_predict_2)

train_rmse_2 = np.sqrt(train_mse_2)
test_rmse_2 = np.sqrt(test_mse_2)

print('train_rmse_2:', train_rmse_2)
print('test_rmse_2:', test_rmse_2)

# train_rmse_2: 34372.6967078
# test_rmse_2: 40591.4270244
