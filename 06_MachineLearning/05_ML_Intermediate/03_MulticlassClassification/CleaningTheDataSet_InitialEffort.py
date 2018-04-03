# This was my first effort at cleaning this data set
# This works but it's not as elegant as the other one

import numpy as np
import pandas as pd

# read, then clean the data set
cars = pd.DataFrame()

# Initial delimit by \t
cars_split_1 = pd.read_csv("auto-mpg.data.txt", delimiter='\t', names=['TheRest', 'car_name'])
cars['car_name'] = cars_split_1['car_name']

# Split using six spaces
cars_split_2 = cars_split_1['TheRest'].str.split(pat='      ', expand=True)
cars_split_2.columns = ['mpg_cylinders_displacement', 'horsepower', 'weight', 'acceleration_year_origin']
cars[['horsepower', 'weight']] = cars_split_2[['horsepower', 'weight']]


# Split using three spaces
cars_split_3 = cars_split_2['mpg_cylinders_displacement'].str.split(pat='   ', expand=True)
cars_split_3.columns = ['mpg', 'cylinders', 'displacement']
cars[['mpg', 'cylinders', 'displacement']] = cars_split_3[['mpg', 'cylinders', 'displacement']]

# Split using three spaces
cars_split_4 = cars_split_2['acceleration_year_origin'].str.split(pat='   ', expand=True)
cars_split_4.columns = ['acceleration', 'year_origin']
cars['acceleration'] = cars_split_4['acceleration']

# Split using two spaces
cars_split_5 = cars_split_4['year_origin'].str.split(pat='  ', expand=True)
cars_split_5.columns = ['year', 'origin']
cars[['year', 'origin']] = cars_split_5[['year', 'origin']]

# Replace '?' in the dataset with nan's
cars = cars.replace('?', np.nan)

# set the dtypes
cars[['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']] = cars[['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']].astype(dtype='float64')
cars[['cylinders', 'year', 'origin']] = cars[['cylinders', 'year', 'origin']].astype(dtype='int64')

# drop all nan's
cars = cars.dropna(axis=0, how='any').copy()
cars = cars.reset_index(drop=True)