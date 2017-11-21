import pandas as pd

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')
geo_routes = pd.read_csv('geo_routes.csv')

print(geo_routes.info())

print(geo_routes.head(5))