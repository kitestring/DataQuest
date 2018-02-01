from scipy.stats import linregress
import pandas as pd

def predicted_y_value(x, m ,b):
    return m * x + b

def calculate_residuals_squared(y, p):
    yp_diff_squared = [(y[i] - p[i]) ** 2 for i in range(len(y))]
    return sum(yp_diff_squared)

wine_quality = pd.read_csv('wine_quality_white.csv')

# We've seen the r_value before -- we'll get to what p_value and stderr_slope are soon -- for now, don't worry about them.
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

# As you can see, these are the same values we calculated (except for slight rounding differences)
print(slope)
print(intercept)

predicted_quality = wine_quality['density'].apply(predicted_y_value, args=(slope,intercept,))

rss = calculate_residuals_squared(wine_quality["quality"], predicted_quality)

print(rss)