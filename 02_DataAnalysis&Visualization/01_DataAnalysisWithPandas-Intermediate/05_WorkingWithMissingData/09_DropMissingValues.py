import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

# Drop all columns in titanic_survival that have missing values and assign the result to drop_na_columns.
drop_na_columns = titanic_survival.dropna(axis=1, how='any')

# Drop all rows in titanic_survival where the columns "age" or "sex" 
# have missing values and assign the result to new_titanic_survival.
new_titanic_survival = titanic_survival.dropna(axis=0, subset=['age', 'sex'], how='any')