import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('fandango_scores.csv')

# Get the frequency distribution for both Fandango_Ratingvalue & IMDB_norm
fandango_distribution = reviews['Fandango_Ratingvalue'].value_counts().sort_index()
imdb_distribution = reviews['IMDB_norm'].value_counts().sort_index()

print(fandango_distribution)
print(imdb_distribution)