import pandas as pd
from sklearn.linear_model import LinearRegression

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

print('a1:', a1)
print('a0:', a0)