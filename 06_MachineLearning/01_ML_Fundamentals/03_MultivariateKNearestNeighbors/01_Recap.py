import pandas as pd
import numpy as np
np.random.seed(1)

# Reads the csv and removes any spaces that might be padding the column headers
dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)

# Randomly resorts the DataFrame to prevent sampling bias
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

# Cleans the 'price' column, removes "$" and "," characters then converts the type to a float
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

# Determine the number of non-null values in each column
print(dc_listings.info())