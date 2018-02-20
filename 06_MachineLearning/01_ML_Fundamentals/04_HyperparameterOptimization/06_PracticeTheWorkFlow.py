import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')

def grid_search_k(features):

    hyper_params = [x for x in range(1,21)]
    mse_values = []
    k_mse_values = {}
    
    for i, k_value in enumerate(hyper_params):
        knn = KNeighborsRegressor(n_neighbors=k_value, algorithm='brute')
        knn.fit(train_df[features], train_df['price'])
        predictions = knn.predict(test_df[features])
        mse_values.append(mean_squared_error(y_true=test_df['price'], y_pred=predictions))
        k_mse_values[mse_values[i]] = k_value
    
    min_mse = min(mse_values)
    k_mse_values[min_mse]
    return k_mse_values[min_mse], min_mse

k, mse = grid_search_k(['accommodates', 'bathrooms'])
two_hyp_mse = {k: mse}

k, mse = grid_search_k(['accommodates', 'bathrooms', 'bedrooms'])
three_hyp_mse = {k: mse}

print('two_hyp_mse:', two_hyp_mse)
print('three_hyp_mse:', three_hyp_mse)