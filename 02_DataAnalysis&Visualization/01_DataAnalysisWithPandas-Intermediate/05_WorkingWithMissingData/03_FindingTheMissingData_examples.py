import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

sex = titanic_survival["sex"]
sex_is_null = pd.isnull(sex)

# This loop show the sex element value with the corresponding isnull return value
# It illustrates the fact that a null value will return a true value
for index, item in enumerate(sex):
	print('%s - %s' % (item, sex_is_null[index]))

# We can use this resultant series to select only the rows that have null values.
sex_null_true = sex[sex_is_null]