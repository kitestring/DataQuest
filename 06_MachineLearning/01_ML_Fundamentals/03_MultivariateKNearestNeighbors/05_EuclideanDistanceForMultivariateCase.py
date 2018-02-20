import pandas as pd
import numpy as np
from scipy.spatial import distance
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

# Remove columns that are either non-ordinal, contain non-numerical values, 
# # contain an excessive number of rows with missing values (cleaning_fee & security_deposit),  or 
# columns that don't directly describe the living space or the listing itself
unnecessary_columns = ['room_type', 'city', 'state', 'latitude', 'longitude', 'zipcode', 
                       'host_response_rate', 'host_acceptance_rate', 'host_listings_count',
                       'cleaning_fee', 'security_deposit']
dc_listings.drop(labels=unnecessary_columns, inplace=True, axis=1)

# Remove rows that have missing values
dc_listings.dropna(axis=0, inplace=True)

# To prevent any single column from having too much of an impact on the distance, 
# we can normalize all of the columns to have a mean of 0 and a standard deviation of 1.
normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())

note = """These methods were written with mass column transformation in mind and when you call mean() or std(), 
the appropriate column means and column standard deviations are used for each value in the Dataframe."""
# print(note)

normalized_listings['price'] = dc_listings['price']


# Let's use the euclidean() function to calculate the Euclidean distance between 2 rows in our dataset to practice.
# Calculate the Euclidean distance using only the accommodates and bathrooms features between the first row 
# and fifth row in normalized_listings using the distance.euclidean() function.

first_listing = normalized_listings.iloc[0][['accommodates', 'bathrooms']]
fifth_listing = normalized_listings.iloc[4][['accommodates', 'bathrooms']]

first_fifth_distance = distance.euclidean(first_listing, fifth_listing)
print(first_fifth_distance)