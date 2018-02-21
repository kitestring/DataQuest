import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# reads and cleans DataFrame
dc_listings = pd.read_csv("dc_airbnb.csv")
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

# Randomizes DataFrame index
np.random.seed(1)
randomized_index = np.random.permutation(len(dc_listings))
dc_listings = dc_listings.loc[randomized_index]

# split the data set into 5 nearly equivalent folds by adding a folds column
dc_listings.set_value(dc_listings.index[0:744], "fold", 1)
dc_listings.set_value(dc_listings.index[744:1488], "fold", 2)
dc_listings.set_value(dc_listings.index[1488:2232], "fold", 3)
dc_listings.set_value(dc_listings.index[2232:2976], "fold", 4)
dc_listings.set_value(dc_listings.index[2976:3723], "fold", 5)