import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=1, dtype='U75'))

is_canada_1986 = (world_alcohol[:, 0] == '1986') & (world_alcohol[:, 2] == 'Canada')
canada_1986 = (world_alcohol[is_canada_1986,:])

print('Extracted Matrix: Is Canada and 1986')
print(canada_1986)

canada_alcohol = canada_1986[:,4]
is_value_empty = canada_alcohol == ''
canada_alcohol[is_value_empty] = '0'
canada_alcohol = canada_alcohol.astype(float)

total_canadian_drinking = canada_alcohol.sum()
print('total_canadian_drinking: ', total_canadian_drinking)