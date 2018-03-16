import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]
target = 'SalePrice'

# instantiate KNeighborRegrssor object
reg = LinearRegression()

# Fit the KNN model using the default k value.
reg.fit(train[['Gr Liv Area']], train[target])

# Get the coefficient and the intercept of the fitted model
a1 = reg.coef_
a0 = reg.intercept_
 
# Make predictions using model.
train_predictions = reg.predict(train[['Gr Liv Area']])
test_predictions = reg.predict(test[['Gr Liv Area']])

# Calculate the root mean square error.
train_mse_2 = mean_squared_error(y_true=train[target], y_pred=train_predictions)
train_rmse_2 = np.sqrt(train_mse_2)

test_mse_2 = mean_squared_error(y_true=test[target], y_pred=test_predictions)
test_rmse_2 = np.sqrt(test_mse_2)

print('train_rmse_2:', train_rmse_2)
print('test_rmse_2:,', test_rmse_2)

# train_rmse_2: 56034.3620014
# test_rmse_2:, 57088.2516126
