import numpy as np
import pandas as pd

# reads and cleans DataFrame
dc_listings = pd.read_csv("dc_airbnb.csv")
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

# Randomizes DataFrame index
np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

# split the data set into 2 nearly equivalent halves
split_one = dc_listings[0:1862].copy()
split_two = dc_listings[1862:].copy()
