from numpy import cov
import pandas as pd

def calc_slope(x, y):
    return cov(x, y)[0, 1] / x.var()

wine_quality = pd.read_csv('wine_quality_white.csv')

m = calc_slope(wine_quality["density"], wine_quality["quality"])

intercept_density = wine_quality["quality"].mean() - (m * wine_quality["density"].mean())

print('intercept_density:', intercept_density)