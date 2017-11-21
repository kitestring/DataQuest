import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))
world_alcohol_dtype = world_alcohol.dtype

# The first 20 rows and columns with index 1 & 2
first_twenty_regions = world_alcohol[0:20,1:3]