import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))

country_is_algeria = (world_alcohol[:,2] == 'Algeria')
country_algeria = (world_alcohol[country_is_algeria,:])


# playing

# vector = np.array([5,10,15,20])
# equal_to_ten = (vector == 10)
# print(vector[equal_to_ten])

# matrix = np.array([
			# [5,10,15],
			# [20,25,30],
			# [35,40,45]
			# ])
			
# second_column_25 = matrix[:,1] == 25
# print second_column_25

# print matrix[second_column_25,:]
			
