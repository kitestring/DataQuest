import pandas as pd
import numpy as np

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:].copy()

def predict_price(new_listing):
    ## DataFrame.copy() performs a deep copy
    temp_df = train_df.copy()
    temp_df['distance'] = temp_df['bathrooms'].apply(lambda X: np.abs(X - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbor_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbor_prices.mean()
    return(predicted_price)

test_df['predicted_price'] = test_df['bathrooms'].apply(lambda X: predict_price(X))

sum_abs_diff = 0
sum_abs_diff_squared = 0
for index, row in test_df.iterrows():
    sum_abs_diff += np.absolute(row['price'] - row['predicted_price'])
    sum_abs_diff_squared += (row['price'] - row['predicted_price']) ** 2

mae = sum_abs_diff / test_df.shape[0]  
mse = sum_abs_diff_squared / test_df.shape[0]
rmse = mse ** 0.5

print('mae:', mae)
print('mse:', mse)
print('rmse:', rmse)

# mae: 65.6461868958
# mse: 18405.444081632548
# rmse: 135.6666653295221