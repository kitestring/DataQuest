import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

# Drop all columns in titanic_survival that have missing values and assign the result to drop_na_columns.
drop_na_columns = titanic_survival.dropna(axis=1, how='any')

# Drop all rows in titanic_survival where the columns "age" or "sex" 
# have missing values and assign the result to new_titanic_survival.
new_titanic_survival = titanic_survival.dropna(axis=0, subset=['age', 'sex'], how='any')

# Sort the new_titanic_survival DataForm by age
new_titanic_survival = new_titanic_survival.sort_values('age', ascending=False)

# Assign the first ten rows from new_titanic_survival to first_ten_rows
first_ten_rows = new_titanic_survival.iloc[0:10]
print(first_ten_rows)

# Assign the fifth row from new_titanic_survival to row_position_fifth
row_position_fifth = new_titanic_survival.iloc[4]
print(row_position_fifth)

# Assign the row with index label 25 from new_titanic_survivalto row_index_25
row_index_25 = new_titanic_survival.loc[25]
print(row_index_25)