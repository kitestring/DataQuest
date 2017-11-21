import pandas as pd

# Write a function that counts the number of null elements in a Series.

def count_nulls(column):
	is_null = pd.isnull(column)
	column_is_true = column[is_null]
	return column_is_true.shape[0]


titanic_survival = pd.read_csv('titanic_survival.csv')

# Use the DataFrame.apply() method along with your function to run across all the columns in titanic_survival
# Assign the result to column_null_count

column_null_count = titanic_survival.apply(count_nulls)
print(column_null_count)