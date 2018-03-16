import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]
target = 'SalePrice'
cols = ['Overall Cond', 'Gr Liv Area']

# instantiate KNeighborRegrssor object
reg = LinearRegression()

# Fit the KNN model using the default k value.
reg.fit(train[cols], train[target])

# Get the coefficient and the intercept of the fitted model
a1 = reg.coef_
a0 = reg.intercept_

print('a1:', a1)
print('a0:', a0)
 
# Make predictions using model.
train_predictions = reg.predict(train[cols])
test_predictions = reg.predict(test[cols])

# Calculate and append the root mean square error.
train_mse_2 = mean_squared_error(y_true=train[target], y_pred=train_predictions)
train_rmse_2 = np.sqrt(train_mse_2)

test_mse_2 = mean_squared_error(y_true=test[target], y_pred=test_predictions)
test_rmse_2 = np.sqrt(test_mse_2)

print('train_rmse_2:', train_rmse_2)
print('test_rmse_2:,', test_rmse_2)


# a1: [-409.56846611  116.73118339]
# a0: 7858.69114639
# train_rmse_2: 56032.3980153
# test_rmse_2:, 57066.9077945