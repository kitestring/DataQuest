import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
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

# Using the KNeighborsRegressor class generate an array of predicted price values
train_df = normalized_listings.iloc[0:2792].copy()
test_df = normalized_listings.iloc[2792:].copy()
features = train_df.columns.tolist()
features.remove('price')

train_features = train_df[features]
train_target = train_df['price']

knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
knn.fit(train_features, train_target)
all_features_predictions = knn.predict(test_df[features])

# Use the mean_squared_error function to calculate the MSE value for the predictions we made in the previous mission
y_true = test_df['price']
y_pred = all_features_predictions

all_features_mse = mean_squared_error(y_true, y_pred)
all_features_rmse = all_features_mse ** 0.5

print('all_features_mse:', all_features_mse)
print('all_features_rmse:', all_features_rmse)
