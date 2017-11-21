# Use the pd.read_csv() function to read "fandango_score_comparison.csv" into a DataFrame object called fandango.
# Then, use the .head() method to print the first two rows

import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

print(fandango.head(2))