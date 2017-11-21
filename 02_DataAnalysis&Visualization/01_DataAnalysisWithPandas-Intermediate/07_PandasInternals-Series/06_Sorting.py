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

# Sort series_custom by index using sort_index(), and assign the result to the variable sc2
sc2 = series_custom.sort_index()

# Sort series_custom by values, and assign the result to the variable sc3
sc3 = series_custom.sort_values()

# Finally, print the first 10 values in sc2 and the first 10 values in sc3
print('\nFirst 10 lines of sc2 = series_custom.sort_index()\n')
print(sc2[0:10])
print('\nFirst 10 lines of sc3 = series_custom.sort_values()\n')
print(sc3[0:10])