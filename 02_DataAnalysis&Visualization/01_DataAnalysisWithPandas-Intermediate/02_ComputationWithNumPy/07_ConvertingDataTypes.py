import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=1, dtype='U75'))

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = '0'

alcohol_consumption = world_alcohol[:,4]

print('alcohol_consumption.dtype: ', alcohol_consumption.dtype)

alcohol_consumption = alcohol_consumption.astype(float)

print('alcohol_consumption.dtype: ', alcohol_consumption.dtype)