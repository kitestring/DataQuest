import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

# Use the pandas dataframe method set_index to assign the FILM
# column as the custom index for the dataframe. Also, specify
# that we don't want to drop the FILM column from the dataframe.
# We want to keep the original dataframe, so assign the new one to fandango_films.

fandango_films = fandango.set_index('FILM', drop=False)

print(fandango_films.loc['Kumiko, The Treasure Hunter (2015)']['IMDB'])
