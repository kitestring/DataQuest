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





# In the following code cell, the criteria_one and criteria_two statements return Boolean Series objects
criteria_one = series_custom > 50
criteria_two = series_custom < 75

# Return a filtered Series object named both_criteria that only contains the values where both criteria are
# true. Use bracket notation and the & operator to obtain this Series object
both_criteria = series_custom[(criteria_one) & (criteria_two)]

# Print the 1st 10 lines of everything to check
print('\ncriteria_one = series_custom > 50\n')
print(criteria_one[0:10])
print('\ncriteria_two = series_custom < 75\n')
print(criteria_two[0:10])
print('\nseries_custom\n')
print(series_custom[0:10])
print('\nboth_criteria\n')
print(both_criteria[0:10])
