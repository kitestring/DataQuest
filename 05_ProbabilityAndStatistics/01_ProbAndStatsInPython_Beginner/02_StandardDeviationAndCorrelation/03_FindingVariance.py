#!~/anaconda3/bin/

import matplotlib.pyplot as plt
import pandas as pd

nba_stats = pd.read_csv('nba_2013.csv')

# Find the mean value of the column.
pf_mean = nba_stats["pts"].mean()
# Initialize variance at zero.
variance = 0
# Loop through each item in the "pts" column.
for p in nba_stats["pts"]:
    # Calculate the difference between the mean and the value.
    difference = p - pf_mean
    # Square the difference. This ensures that the result isn't negative.
    # If we didn't square the difference, the total variance would be zero.
    # ** in python means "raise whatever comes before this to the power of whatever number is after this."
    square_difference = difference ** 2
    # Add the difference to the total.
    variance += square_difference
# Average the total to find the final variance.sf
point_variance = variance / len(nba_stats["pts"]) 
print(point_variance)