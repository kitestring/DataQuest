import pandas as pd

def calc_E_distances(row, col, compare_value=3):
    return abs(row[col] - compare_value)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)

dc_listings['distance'] = dc_listings.apply(calc_E_distances, args=('accommodates',), axis=1)

print(dc_listings['distance'].value_counts())