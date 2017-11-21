import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

# Return a dataframe containing just the first and last rows, and assign it to first_last
first_row = 0
last_row = fandango.shape[0] - 1

first_last = fandango.iloc[[first_row , last_row]]

print(first_last)