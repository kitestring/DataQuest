import pandas
import matplotlib.pyplot as plt
import os
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

print(iris.head())

# There are 2 species
print(iris.species.unique())
print(iris.info())

iris.hist()
plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig1.png'
plt.savefig(plot_file_name, bbox_inches='tight')
plt.show()