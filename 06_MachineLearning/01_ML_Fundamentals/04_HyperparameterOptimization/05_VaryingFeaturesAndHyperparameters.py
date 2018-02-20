import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')
features = train_df.columns.tolist()
features.remove('price')

hyper_params = [x for x in range(1,21)]
mse_values = []
k_mse_values = {}

for i, k_value in enumerate(hyper_params):
    knn = KNeighborsRegressor(n_neighbors=k_value, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(y_true=test_df['price'], y_pred=predictions))
    k_mse_values[mse_values[i]] = k_value
    print('When k={kv}, mse={mse}'.format(kv=k_value, mse=mse_values[i]))

min_mse = min(mse_values)
print('\nWhen k={kv}, the mse value is at the minimum'.format(kv=k_mse_values[min_mse]))
    
plt.scatter(x=hyper_params, y=mse_values)
plt.show()

# Best k value is:
# When k=11, mse=14711.46334583815