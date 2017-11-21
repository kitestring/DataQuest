import numpy as np
from pandas import read_csv
from pandas import Series

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,6,5,4,3,2,1,0])

z = np.add(x,y)

print(x)
print(y)
print(z)

print('\nOk, here\'s the DATAQUEST example\n')

fandango = read_csv('fandango_score_comparison.csv')

# Select the FILM column, assign it to the variable series_film, and print the first five values
# Convert 'series_film' the pandas Series Object to an ndarray or ndarray-like depending on the dtype
series_film = fandango['FILM']
film_names = series_film.values

# Then, select the RottenTomatoes column, assign it to the variable series_rt, and print the first five values
# Convert 'series_film' the pandas Series Object to an ndarray or ndarray-like depending on the dtype
series_rt = fandango['RottenTomatoes']
rt_scores = series_rt.values

# Instantiate a new Series object, which takes in a data parameter and an index parameter.
series_custom = Series(index=film_names, data=rt_scores)






# Add each value with each other
print(np.add(series_custom, series_custom))
print('\n\n')

# Apply sine function to each value
print(np.sin(series_custom))
print('\n\n')

# Return the highest value (will return a single value, not a Series)
print(np.max(series_custom))