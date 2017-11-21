# Use the Low_wage_jobs and Total columns to calculate the proportion of
# recent college graduates that worked low wage jobs.

# I'll need to know the total number of graduates and the total number
# of graduates that are working low wage jobs

import pandas as pd

# Read recent-grads.csv into a DataFrame object, and assign it to recent_grads
recent_grads = pd.read_csv('recent-grads.csv')

low_wage_percent = recent_grads['Low_wage_jobs'].sum() / recent_grads['Total'].sum()

print('%f%% of recent grads worked low wage jobs' % round(low_wage_percent*100,2))