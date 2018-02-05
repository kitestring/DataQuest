import pandas as pd

flags = pd.read_csv('flags.csv')

countries = flags.shape[0]

reds = flags['red'].sum()
oranges = flags['orange'].sum()
red_and_orange = flags[(flags['red'] == 1) & (flags['orange'] == 1)].shape[0]

red_or_orange = ((reds/countries) + (oranges/countries)) - (red_and_orange/countries)
print(red_or_orange)

non_zero_stripes = flags[flags['stripes'] >= 1].shape[0]
non_zero_bars = flags[flags['bars'] >= 1].shape[0]
non_zero_stripes_AND_non_zero_bars = flags[(flags['stripes'] >= 1) & (flags['bars'] >= 1)].shape[0]

stripes_or_bars = ((non_zero_stripes/countries) + (non_zero_bars/countries)) - (non_zero_stripes_AND_non_zero_bars/countries)
print(stripes_or_bars)