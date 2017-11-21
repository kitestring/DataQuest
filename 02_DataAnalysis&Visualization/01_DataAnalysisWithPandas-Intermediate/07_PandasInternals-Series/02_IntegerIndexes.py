import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

# Select the FILM column, assign it to the variable series_film, and print the first five values
series_film = fandango['FILM']
print(series_film[0:5])

# Then, select the RottenTomatoes column, assign it to the variable series_rt, and print the first five values
series_rt = fandango['RottenTomatoes']
print(series_rt[0:5])