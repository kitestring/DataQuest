from numpy import cov
import pandas as pd

def calc_slope(x, y):
    return cov(x, y)[0, 1] / x.var()

def calc_intercept(x, y, slope):
    return y.mean() - (slope * x.mean())

def predicted_y_value(x, m ,b):
    return m * x + b

wine_quality = pd.read_csv('wine_quality_white.csv')

m = calc_slope(wine_quality["density"], wine_quality["quality"])
y = calc_intercept(wine_quality["density"], wine_quality["quality"], m)

predicted_quality = wine_quality['density'].apply(predicted_y_value, args=(m,y,))

print(predicted_quality)

