import pandas as pd
import numpy as np

def calc_E_distances(row, col, compare_value):
    return abs(row[col] - compare_value)

def remove_commas_dollarsigns(row, col):
    x = row[col].replace(',',"")
    return  x.replace('$',"")

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    
    # Calculates the Euclidean distance based upon the number of people the location can accommodate
    temp_df['distance'] = temp_df.apply(calc_E_distances, args=('accommodates',new_listing,), axis=1)
    
    # Randomizes the DataFrame then sorts based upon the Euclidean distance (distance) column
    np.random.seed(1)
    temp_df = temp_df.loc[np.random.permutation(len(dc_listings))]
    temp_df = temp_df.sort_values('distance')
    
    # Return the mean of the 1st 5 (the k value for this mission) price values
    return temp_df.iloc[0:5]['price'].mean()

# Reads csv and removes any spaces that might be padding the column headers
dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)

# Cleans the price column (removes "," and "$" characters) and converts the series to a float
dc_listings['price'] = dc_listings.apply(remove_commas_dollarsigns, args=('price',), axis=1)
dc_listings['price'] = dc_listings['price'].astype('float')

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)

print('acc_one:', acc_one)
print('acc_two:', acc_two)
print('acc_four:', acc_four)