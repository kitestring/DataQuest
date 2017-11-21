from pandas import read_csv
from pandas import Series
import numpy as np

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





# Normalize series_custom (which is currently on a 0 to 100-point scale)
# to a 0 to 5-point scale by dividing each value by 20
# Assign the new normalized Series object to series_normalized
series_normalized = np.divide(series_custom, 20)

# Print the 1st five rows of series_custom & series_normalized to verify
print('\nseries_custom\n')
print(series_custom[0:5])
print('\nseries_normalized\n')
print(series_normalized[0:5])