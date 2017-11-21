import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ','))

world_alcohol_dtype = world_alcohol.dtype

print (world_alcohol_dtype)