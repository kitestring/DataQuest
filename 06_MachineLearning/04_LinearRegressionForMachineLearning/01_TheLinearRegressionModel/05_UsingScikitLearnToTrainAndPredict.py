# Import and instantiate a linear regression model.
# Fit a linear regression model that uses the feature and target columns we explored in the last 2 screens. Use the default arguments.
# Display the coefficient and intercept of the fitted model using the coef_ and intercept_ attributes.
# Assign a1 to a1 and a0 to a0.

import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]
target = 'SalePrice'

# instantiate KNeighborRegrssor object
reg = LinearRegression()

# Fit the KNN model using the default k value.
reg.fit(train['Gr Liv Area'].values.reshape(-1, 1), train[target].values.reshape(-1, 1))

# Get the coefficient and the intercept of the fitted model
a1 = reg.coef_
a0 = reg.intercept_

print('a1:', a1)
print('a0:', a0)