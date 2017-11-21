''' We can use the reindex() method to sort series_custom
	alphabetically by film. To accomplish this, we need to:
			Return a list representation of the current index using tolist().
			Sort the index with sorted()
			Use reindex() to set the newly-ordered index'''

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




# Return a list representation of the current index using tolist()
original_index = series_custom.index

# Sort the index with sorted()
new_index = sorted(original_index)

# then pass the result in to the Series method reindex()
# Store the result in a variable named sorted_by_index
sorted_by_index = series_custom.reindex(new_index)