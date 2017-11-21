import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=1, dtype='U75'))

print(world_alcohol.shape)

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = '0'

print(world_alcohol.shape)