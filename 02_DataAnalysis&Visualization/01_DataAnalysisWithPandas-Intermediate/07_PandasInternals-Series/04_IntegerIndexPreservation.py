# When it comes to indexes, Series objects act like both dictionaries
# and lists. We can access values with our custom index (like the
# keys in a dictionary), or the integer index (like the index in a list).

from pandas import read_csv
from pandas import Series

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

# Assign the values in series_custom at indexes 5 through 10 to the variable fiveten.
# Then, print fiveten to verify that you can still use integer values for selection.
fiveten = series_custom[5:11]
print(fiveten)