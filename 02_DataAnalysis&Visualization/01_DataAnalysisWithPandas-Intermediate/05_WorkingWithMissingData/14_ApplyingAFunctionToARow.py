import pandas as pd

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
print(age_labels)

raw_input("\nEnter To Continue\n")

# Extra credit,
# Count the number of each type as assign result to age_labels_counts
age_labels_counts = age_labels.value_counts()
print(age_labels_counts)

raw_input("\nEnter To Continue\n")

# Extract the index labels from the series to a list
# Then iterate through the list and print the index with the count
for index_label in age_labels_counts.index.tolist():
	print('There are %d %s' % (age_labels_counts[index_label], index_label))