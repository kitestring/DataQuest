import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

# Count how many values in the "age" column have null values:

age = titanic_survival['age']
age_is_null = pd.isnull(age)

# Grabs the values from the age series where age_is_null = True, thus is NaN
age_null_true = age[age_is_null]

# counts the number of rows in the age_null_count series which equals the total number of NaN's in the age series
age_null_count = age_null_true.shape[0]
print age_null_count