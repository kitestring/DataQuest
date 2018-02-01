from scipy.stats import linregress
import numpy as np
import pandas as pd

def standard_error_proportion(y, p, standard_error, n):
    yp_diff = [y[i] - p[i] for i in range(len(y))]
    standard_errors = standard_error * n
    within_n_standard_errors = [i for i in yp_diff if i <= standard_errors and i >= -standard_errors]
    return len(within_n_standard_errors) / len(y)

wine_quality = pd.read_csv('wine_quality_white.csv')

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)

standard_error = (rss/(len(wine_quality["quality"]) - 2)) ** 0.5

within_one = standard_error_proportion(wine_quality["quality"], predicted_y, standard_error, 1)
within_two = standard_error_proportion(wine_quality["quality"], predicted_y, standard_error, 2)
within_three = standard_error_proportion(wine_quality["quality"], predicted_y, standard_error, 3)

print(within_one)
print(within_two)
print(within_three)