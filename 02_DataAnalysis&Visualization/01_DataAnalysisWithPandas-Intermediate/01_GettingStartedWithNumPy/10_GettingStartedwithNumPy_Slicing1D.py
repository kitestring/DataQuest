import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))
world_alcohol_dtype = world_alcohol.dtype

# All rows and the first 2 columns
first_two_columns = world_alcohol[:,0:2]
# The first 10 rows and the first column
first_ten_years = world_alcohol[0:10,0]
# The first 10 rows and all the columns
first_ten_rows = world_alcohol[0:10,:]

