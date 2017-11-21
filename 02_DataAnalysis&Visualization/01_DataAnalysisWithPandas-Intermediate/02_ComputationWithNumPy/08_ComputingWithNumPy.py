import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=1, dtype='U75'))

is_value_empty = world_alcohol[:, 4] == ''
world_alcohol[is_value_empty, 4] = '0'

alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

print('total_alcohol: ', total_alcohol)
print('average_alcohol: ', average_alcohol)