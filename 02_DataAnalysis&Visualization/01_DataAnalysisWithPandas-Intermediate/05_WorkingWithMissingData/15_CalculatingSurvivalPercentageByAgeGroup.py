import pandas as pd
import numpy as np

# Create a function that returns the string "minor" if
# someone is under 18, "adult" if they are equal to or
# over 18, and "unknown" if their age is null
def age_type(row):
	age = row['age']
	if pd.isnull(age):
		return 'unknown'
	elif age < 18:
		return 'minor'
	else:
		return 'adult'
		
titanic_survival = pd.read_csv('titanic_survival.csv')
		
# Iterates through each row and deterines the age type of each passenger
# Then, use the function along with .apply() to find the correct
# label for everyone in the titanic_survival dataframe
# Assign the result to age_labels
age_labels = titanic_survival.apply(age_type, axis=1)

# Add the age_labels series as a column called 'age_labels' to the titanic_survival dataframe
titanic_survival['age_labels'] = age_labels

# Create a pivot table that calculates the mean survival
# chance("survived") for each age group ("age_labels") of the dataframe titanic_survival
# Assign the resulting Series object to age_group_survival
age_group_survival = titanic_survival.pivot_table(index='age_labels', values='survived', aggfunc=np.mean)
print(age_group_survival)