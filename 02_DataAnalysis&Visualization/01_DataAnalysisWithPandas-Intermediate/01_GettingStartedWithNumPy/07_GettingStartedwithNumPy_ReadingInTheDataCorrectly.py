import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))

world_alcohol_dtype = world_alcohol.dtype

print (world_alcohol)
print (world_alcohol_dtype)