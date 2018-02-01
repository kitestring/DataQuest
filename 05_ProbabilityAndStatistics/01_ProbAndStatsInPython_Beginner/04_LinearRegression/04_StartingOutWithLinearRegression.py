# The wine quality data is loaded into wine_quality
from numpy import cov
import pandas as pd

wine_quality = pd.read_csv('wine_quality_white.csv')

slope_density = cov(wine_quality["density"], wine_quality["quality"])[0, 1] / wine_quality["density"].var()
print(slope_density)