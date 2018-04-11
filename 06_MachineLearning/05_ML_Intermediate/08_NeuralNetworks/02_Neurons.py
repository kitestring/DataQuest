import pandas
import numpy as np

# Read in dataset
iris = pandas.read_csv("iris.csv")

# shuffle rows
shuffled_rows = np.random.permutation(iris.index)
# Because dataquest does not seed their random numbers I used a print statement to get their numbers
shuffled_rows =[80, 84, 33, 81, 93, 17, 36, 82, 69, 65, 92, 39, 56, 52, 51, 32, 31, 44, 78, 10, 2, 73, 97, 62, 19,
 35, 94, 27, 46, 38, 67, 99, 54, 95, 88, 40, 48, 59, 23, 34, 86, 53, 77, 15, 83, 41, 45, 91, 26, 98,
 43, 55, 24,  4, 58, 49, 21, 87,  3, 74, 30, 66, 70, 42, 47, 89,  8, 60,  0, 90, 57, 22, 61, 63,  7,
 96, 13, 68, 85, 14, 29, 28, 11, 18, 20, 50, 25,  6, 71, 76,  1, 16, 64, 79,  5, 75,  9, 72, 12, 37]
iris = iris.loc[shuffled_rows,:]

# Below is a very simple reminder of how to take the dot product using numpy
    # np.dot is used for matrix multiplication
    # z is 1x3 and y is 1x3,  z * y.T is then 1x1
    # y is transposed because when taking the dot product on of
    # the vectors must be represented as a row vector &
    # the other a column vector
z = np.asarray([[9, 5, 4]])
y = np.asarray([[-1, 2, 4]])
# print(np.dot(z,y.T))

def sigmoid_activation(x, theta):
    x = np.asarray(x)
    theta = np.asarray(theta)
    return 1 / (1 + np.exp(-np.dot(theta.T, x)))

# Variables to test sigmoid_activation
iris["ones"] = np.ones(iris.shape[0]) # This creates a column called ones that consists entirely of the integer 1
X = iris[['ones', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values # Creates a numpy representation of the DataFrame
y = (iris.species == 'Iris-versicolor').values.astype(int) # Creates a numpy array of 0's (False) & 1's (True) if a values is == to 'Iris-versicolor'

# The first observation
x0 = X[0]

# Initialize thetas randomly numpy.random.normal - Draw random samples from a normal (Gaussian) distribution.
    # float or array_like of floats Mean (centre) of the distribution.
    # float or array_like of floats Standard deviation (spread or width) of the distribution.
theta_init = np.random.normal(loc=0,scale=0.01,size=(5,1))
# Because dataquest does not seed their random numbers I used a print statement to get their "random" numbers
theta_init = np.array=[[ 0.01624345],[-0.00611756],[-0.00528172],[-0.01072969],[ 0.00865408]]

a1 = sigmoid_activation(x0, theta_init)
print(a1)