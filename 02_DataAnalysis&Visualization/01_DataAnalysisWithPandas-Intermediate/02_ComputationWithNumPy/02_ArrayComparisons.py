import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))

countries = world_alcohol[:,2]
countries_canada = 'Canada' == countries

years = world_alcohol[:,0]
years_1984 = years == '1984'


# playing

# vector = np.array([5,10,15,20])

# print vector == 10

# matrix = ([
			# [5,10,15],
			# [20,25,30],
			# [35,40,45]
			# ])
			
# print matrix == 25