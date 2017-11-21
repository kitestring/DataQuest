import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

age_with_nulls = titanic_survival['age']
age_is_null = pd.isnull(age_with_nulls)

age_no_nulls = age_with_nulls[age_is_null == False]

correct_mean_age = age_no_nulls.mean()

print(correct_mean_age)
print(age_with_nulls.mean())