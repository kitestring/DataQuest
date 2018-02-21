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

# Column(s) that will be used to train the model
features = ['accommodates']

def rmse_knn(df, testing_fold, features, predictive_item):
    # returns the root mean squared error for a K-Nearest Neighbors fit
    # The training fold is all rows in the df where fold != testing_fold
    # The testing fold is all rows in the df where fold == testing_fold
    
    training_df = df[df["fold"] != testing_fold]
    testing_df = df[df["fold"] == testing_fold]
    
    knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
    knn.fit(training_df[features], training_df[predictive_item])
    labels = knn.predict(testing_df[features])
    return mean_squared_error(y_true=testing_df[predictive_item], y_pred=labels) ** 0.5

iteration_one_rmse = rmse_knn(df=dc_listings, testing_fold=1, features=features, predictive_item='price')

print('iteration_one_rmse:', iteration_one_rmse)

# iteration_one_rmse: 105.064985011