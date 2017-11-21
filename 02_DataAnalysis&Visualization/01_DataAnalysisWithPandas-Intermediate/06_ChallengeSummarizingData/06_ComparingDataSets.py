# Calculate the number of majors where recent graduates did better than the overall population

# For each major code determine if recent grads have a lower unemployment rate than the overall population
# Count the number of majors where this is true

import pandas as pd

# Read all-ages.csv & recent-grads.csv assign to into a DataFrame object, called all_ages & recent_grads respectively
all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')

# Instantiate rg_lower_count which will be used to increment (count) the 
# number of majors where recent grads have a lower unemployment rate than 
# majors of all ages 
rg_lower_count = 0

# Iterate through the Major_codes and compare the unemployment rates of all ages
# and recent grads.  If recent grads have a lower unemployment rate then
# increment the rg_lower_count value
for major_code in all_ages['Major_code']:
	all_ages_row = all_ages.loc[all_ages['Major_code'] == major_code]
	recent_grads_row = recent_grads.loc[recent_grads['Major_code'] == major_code]
	
	if float(recent_grads_row['Unemployment_rate']) < float(all_ages_row['Unemployment_rate']):
		rg_lower_count += 1

print(rg_lower_count)