import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Basemap constructors:
# projection: the map projection
# llcrnrlat: latitude of lower left hand corner of the desired map domain
# urcrnrlat: latitude of upper right hand corner of the desired map domain
# llcrnrlon: longitude of lower left hand corner of the desired map domain
# urcrnrlon: longitude of upper right hand corner of the desired map domain

m = Basemap(projection="merc", llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)