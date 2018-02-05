import pandas as pd

flags = pd.read_csv('flags.csv')
print(flags.head(2))

most_bars_country = flags['name'][flags['bars'].max() == flags['bars']]
print(most_bars_country)

highest_population_country = flags['name'][flags['population'].max() == flags['population']]
print(highest_population_country)