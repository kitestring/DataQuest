import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

# Use the pandas dataframe method set_index to assign the FILM
# column as the custom index for the dataframe. Also, specify
# that we don't want to drop the FILM column from the dataframe.
# We want to keep the original dataframe, so assign the new one to fandango_films.

fandango_films = fandango.set_index('FILM', drop=False)

# Select the following movies from fandango_films (in the order in which they appear), and assign them to best_movies_ever:
		# "The Lazarus Effect (2015)"
		# "Gett: The Trial of Viviane Amsalem (2015)"
		# "Mr. Holmes (2015)"
		
best_movies_ever_index = ["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[best_movies_ever_index]
print(best_movies_ever)