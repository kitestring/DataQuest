import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))
world_alcohol_dtype = world_alcohol.dtype

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]


# Just playing around here
# print 'world_alcohol.shape: ', world_alcohol.shape

# print ('Raw unedited data')
# print (world_alcohol)
# print (world_alcohol_dtype)

# uruguay_other_1986 = world_alcohol [1,4]
# third_country = world_alcohol [2,2]
# print ('uruguay_other_1986: ',uruguay_other_1986)
# print ('third_country: ',third_country)

# print('/nSlicing Arrays')

# sliced_array = world_alcohol[:,2]
# sliced_array.sort
# sliced_array = np.unique(sliced_array)
# for item in sliced_array:
	# print(item)