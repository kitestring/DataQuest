import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

airlines = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')

# Basemap constructors:
# projection: the map projection
# llcrnrlat: latitude of lower left hand corner of the desired map domain
# urcrnrlat: latitude of upper right hand corner of the desired map domain
# llcrnrlon: longitude of lower left hand corner of the desired map domain
# urcrnrlon: longitude of upper right hand corner of the desired map domain

# Create a new basemap instance with the specific map projection we want to use and how much of the map we want included.

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

longitudes = airports['longitude'].tolist()
latitudes = airports['latitude'].tolist()

# Convert spherical coordinates to Cartesian coordinates using the basemap instance
x, y = m(longitudes, latitudes)

# Use the matplotlib and basemap methods to customize the map
m.scatter(x, y, s=1)

plt.show()