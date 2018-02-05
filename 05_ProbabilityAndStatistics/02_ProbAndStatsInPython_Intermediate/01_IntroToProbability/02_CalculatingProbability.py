import pandas as pd

flags = pd.read_csv('flags.csv')
total_countries = flags.shape[0]

# Determine the probability of a country having a flag with the color orange in it.
orange_probability = flags[flags["orange"] == 1].shape[0] / total_countries
print('orange_probability:', orange_probability)

# Determine the probability of a country having a flag with more than 1 stripe in it.
stripe_probability = flags[flags["stripes"] > 1].shape[0] / total_countries
print('stripe_probability:', stripe_probability)