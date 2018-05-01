# pages 40-xh' in the hand written notes for context

import pandas
from sklearn.linear_model import LinearRegression
import numpy as np

# Read data from csv
pga = pandas.read_csv("pga.csv")

# Normalize the data
pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()

# We can add a dimension to an array by using np.newaxis
print("Shape of the series:", pga.distance.shape)
print("Shape with newaxis:", pga.distance[:, np.newaxis].shape)

# The added dimension is done because
# The X variable in LinearRegression.fit() must have 2 dimensions
lr = LinearRegression()
model = lr.fit(pga.distance[:, np.newaxis], pga.accuracy)
print(lr.coef_)
theta1 = lr.coef_[0]