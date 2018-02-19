import pandas as pd
import numpy as np

def calc_E_distances(row, col, compare_value=3):
    return abs(row[col] - compare_value)

def remove_commas_dollarsigns(row, col):
    x = row[col].replace(',',"")
    return  x.replace('$',"")

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)

dc_listings['distance'] = dc_listings.apply(calc_E_distances, args=('accommodates',), axis=1)

np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values('distance')


#  This gets the

dc_listings['price'] = dc_listings.apply(remove_commas_dollarsigns, args=('price',), axis=1)
dc_listings['price'] = dc_listings['price'].astype('float')
mean_price = dc_listings.iloc[0:5]['price'].mean()
print(mean_price)