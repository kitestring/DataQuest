import pandas as pd

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)

first_distance = abs(dc_listings.loc[0]['accommodates'] - 3)
print(first_distance)