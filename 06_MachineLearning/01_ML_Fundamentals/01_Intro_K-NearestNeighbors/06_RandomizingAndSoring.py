import pandas as pd
import numpy as np

def calc_E_distances(row, col, compare_value=3):
    return abs(row[col] - compare_value)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)

dc_listings['distance'] = dc_listings.apply(calc_E_distances, args=('accommodates',), axis=1)

np.random.seed(1)
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
dc_listings = dc_listings.sort_values('distance')
print(dc_listings.iloc[0:10][['price', 'distance']])


# without randomizing
#         price  distance
# 3722  $110.00         0
# 2197  $135.00         0
# 549   $110.00         0
# 2199  $100.00         0
# 2202  $125.00         0
# 3072   $89.00         0
# 1311  $100.00         0
# 1309   $70.00         0
# 2219  $249.00         0
# 3060  $165.00         0

# with randomizing
#         price  distance
# 577   $185.00         0
# 2166  $180.00         0
# 3631  $175.00         0
# 71    $128.00         0
# 1011  $115.00         0
# 380   $219.00         0
# 943   $125.00         0
# 3107  $250.00         0
# 1499   $94.00         0
# 625   $150.00         0