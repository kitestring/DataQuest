import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

# Use the head method to return the first two rows in the dataframe, then display them with the print function.
print('\nPeak at 1st 2 rows using head\n')
print(fandango.head(2))

# Use the index attribute to return the index of the dataframe, and display it with the print function.
print('\nHere\'s fandano\'s Indexes\n')
print(fandango.index.values)
print('\nHere\'s fandango\'s Indexes as a list\n')
print(fandango.index.tolist())