# pages 40-xh' in the hand written notes for context

import pandas
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

# Read data from csv
pga = pandas.read_csv("pga.csv")

# Normalize the data
pga.distance = (pga.distance - pga.distance.mean()) / pga.distance.std()
pga.accuracy = (pga.accuracy - pga.accuracy.mean()) / pga.accuracy.std()

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

theta0s = np.linspace(-2,2,100)
theta1s = np.linspace(-2,2, 100)
COST = np.empty(shape=(100,100))

# We must create variables to represent each possible pair of points in x (theta0) and y (theta1s)
# ie. (-10, 10), (-10, -9.8), ... (0, 0), ... ,(10, 9.8), (10,9.8)
# x and y need to be transformed to 100x100 matrices to represent these coordinates
# np.meshgrid will build a coordinate matrices of x and y
X, Y = np.meshgrid(theta0s, theta1s)

for i in range(100):
    for j in range(100):
        COST[i,j] = cost(theta0s[i], theta1s[j], pga.distance, pga.accuracy)
    print(i)
        
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X=X,Y=Y,Z=COST)

plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig1.png'
plt.savefig(plot_file_name, bbox_inches='tight')
plt.show()

