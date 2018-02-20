import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

hyper_params = [x for x in range(1,6)]
mse_values = []

for i, k in enumerate(hyper_params):
    knn = KNeighborsRegressor(n_neighbors=k,algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df['price'], predictions))
    print('When k={kv}, mse={mse}'.format(kv=k, mse=mse_values[i]))