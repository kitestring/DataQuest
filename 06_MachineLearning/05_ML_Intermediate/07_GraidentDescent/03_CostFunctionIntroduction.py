# pages 40-xh' in the hand written notes for context

import pandas
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import os

# Read data from csv
pga = pandas.read_csv("pga.csv")

# Normalize the data
pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()

# The added dimension is done because
# the X variable in LinearRegression.fit() must have 2 dimensions
lr = LinearRegression()
model = lr.fit(pga.distance[:, np.newaxis], pga.accuracy)
theta1 = lr.coef_[0]


# The cost function of a single variable linear model
def cost(theta0, theta1, x, y):
    # Initialize cost
    J = 0
    # The number of observations
    m = len(x)
    # Loop through each observation
    for i in range(m):
        # Compute the hypothesis 
        h = theta1 * x[i] + theta0
        # Add to cost
        J += (h - y[i])**2
    # Average and normalize cost
    J /= (2*m)
    return J

# The cost for theta0=0 and theta1=1
print('The cost for theta0=0 and theta1=1')
print(cost(0, 1, pga.distance, pga.accuracy))

theta0 = 100
theta1s = np.linspace(-3,2,100)

costs = []

print("Question:\nWhy are we just varying theta1 and leaving theta0 = 100?\nI guessing that we'll vary theta0 later?")

for t1 in theta1s:
    costs.append(cost(theta0, t1, pga.distance, pga.accuracy))

plt.plot(theta1s, costs)
plt.xlabel('theta 1')
plt.ylabel('cost')
plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig1.png'
plt.savefig(plot_file_name, bbox_inches='tight')
plt.show()