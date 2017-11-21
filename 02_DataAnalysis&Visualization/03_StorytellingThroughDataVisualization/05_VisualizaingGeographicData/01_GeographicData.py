import pandas as pd

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')

print('******airlines**********')
print(airlines.iloc[0])
print('\n\n**************airports*************')
print(airports.iloc[0])
print('\n\n**************routes*************')
print(routes.iloc[0])


# What's the best way to link the data from these 3 different datasets together?
# ???

# What are the formats of the latitude and longitude values?
# float or double