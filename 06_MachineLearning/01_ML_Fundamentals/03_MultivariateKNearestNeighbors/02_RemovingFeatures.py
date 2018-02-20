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

# Remove columns that are either non-ordinal, contain non-numerical values, or   
# columns that don't directly describe the living space or the listing itself
unnecessary_columns = ['room_type', 'city', 'state', 'latitude', 'longitude', 'zipcode', 
                       'host_response_rate', 'host_acceptance_rate', 'host_listings_count']
dc_listings.drop(labels=unnecessary_columns, inplace=True, axis=1)
print(dc_listings.info())

