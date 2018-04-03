import numpy as np
import pandas as pd

# Read text file and delimit with whitespace
headers = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'car_name']
cars = pd.read_csv("auto-mpg.data.txt", delim_whitespace=True, names=headers)

# Replace '?' in the dataset with nan's
cars = cars.replace('?', np.nan)

# set the dtypes
cars[['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']] = cars[['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']].astype(dtype='float64')
cars[['cylinders', 'year', 'origin']] = cars[['cylinders', 'year', 'origin']].astype(dtype='int64')

# drop all rows that have nan's
cars = cars.dropna(axis=0, how='any')
cars = cars.reset_index(drop=True)

# write the df to csv, as is
cars.to_csv('cars.csv')
