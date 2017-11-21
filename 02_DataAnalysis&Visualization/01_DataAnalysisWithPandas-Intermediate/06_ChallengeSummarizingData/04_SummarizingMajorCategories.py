import pandas as pd
import numpy as np

# Read all-ages.csv into a DataFrame object, and assign it to all_ages
all_ages = pd.read_csv('all-ages.csv')

# Read recent-grads.csv into a DataFrame object, and assign it to recent_grads
recent_grads = pd.read_csv('recent-grads.csv')

# Create the dictionaries to how the values
aa_cat_counts = {}
rg_cat_counts = {}

# Return the unique values in Major_category
all_ages_unique_major_categories = all_ages['Major_category'].unique()
recent_grads_unique_major_categories = recent_grads['Major_category'].unique()

# Count the number of studens in each Major_category for both groups
all_ages_major_summation = all_ages.pivot_table(index='Major_category', values='Total', aggfunc=np.sum)
recent_grads_major_summation = recent_grads.pivot_table(index='Major_category', values='Total', aggfunc=np.sum)

# Add each key(major) and value(summation) to the dictionary
for major in all_ages_unique_major_categories:
	aa_cat_counts[major] = all_ages_major_summation.loc[major]
	
for major in recent_grads_unique_major_categories:
	rg_cat_counts[major] = recent_grads_major_summation.loc[major]
	
# Review each dictionary
print('\n***aa_cat_counts***\n')
for major in aa_cat_counts:
	print('%s\t%d' %(major, aa_cat_counts[major]))

print('\n***rg_cat_counts***\n')	
for major in rg_cat_counts:
	print('%s\t%d' %(major, rg_cat_counts[major]))