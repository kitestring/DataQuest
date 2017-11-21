import pandas as pd

# Read all-ages.csv into a DataFrame object, and assign it to all_ages
all_ages = pd.read_csv('all-ages.csv')

# Read recent-grads.csv into a DataFrame object, and assign it to recent_grads
recent_grads = pd.read_csv('recent-grads.csv')

# Display the first five rows of all_ages 
print('\n---1st 5 rows of all_ages---\n')
print(all_ages.iloc[0:5])
print('\n---Columns of all_ages---\n')
print(all_ages.columns)

# Display the first five rows of recent_grads
print('\n---1st 5 rows of recent_grads---\n')
print(recent_grads.iloc[0:5])
print('\n---Columns of recent_grads---\n')
print(recent_grads.columns)