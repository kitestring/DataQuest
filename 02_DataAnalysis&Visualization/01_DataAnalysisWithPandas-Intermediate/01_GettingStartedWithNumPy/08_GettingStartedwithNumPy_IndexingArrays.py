import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter = ',', skip_header=1, dtype='U75'))

world_alcohol_dtype = world_alcohol.dtype

print ('Raw unedited data')
print (world_alcohol)
print (world_alcohol_dtype)

uruguay_other_1986 = world_alcohol [1,4]
third_country = world_alcohol [2,2]
print ('uruguay_other_1986: ',uruguay_other_1986)
print ('third_country: ',third_country)