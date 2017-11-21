from pandas import read_csv
from pandas import Series 

fandango = read_csv('fandango_score_comparison.csv')

# Select the FILM column, assign it to the variable series_film, and print the first five values
series_film = fandango['FILM']

# Convert 'series_film' the pandas Series Object to an ndarray or ndarray-like depending on the dtype
film_names = series_film.values

# Then, select the RottenTomatoes column, assign it to the variable series_rt, and print the first five values
series_rt = fandango['RottenTomatoes']

# Convert 'series_film' the pandas Series Object to an ndarray or ndarray-like depending on the dtype
rt_scores = series_rt.values

# Instantiate a new Series object, which takes in a data parameter and an index parameter.
series_custom = Series(index=film_names, data=rt_scores)

# print the RT Scores from 'Minions (2015)' and 'Leviathan (2014)' from the series_custom Series Object
print(series_custom[['Minions (2015)', 'Leviathan (2014)']])