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

# split the data set into 2 nearly equivalent halves
split_one = dc_listings[0:1862].copy()
split_two = dc_listings[1862:].copy()

# Dividing the halves into test and training sets
train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

# Column(s) that will be used to train the model
features = ['accommodates']

def rmse_knn(training_df, testing_df, features, predictive_item):
    # returns the root mean squared error for a K-Nearest Neighbors fit
    knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
    knn.fit(training_df[features], training_df[predictive_item])
    predictions = knn.predict(testing_df[features])
    return mean_squared_error(y_true=testing_df[predictive_item], y_pred=predictions) ** 0.5

iteration_one_rmse = rmse_knn(training_df=train_one, testing_df=test_one, features=features, predictive_item='price')
iteration_two_rmse = rmse_knn(training_df=train_two, testing_df=test_two, features=features, predictive_item='price')

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])
print('avg_rmse:', avg_rmse)

# avg_rmse: 128.962547329