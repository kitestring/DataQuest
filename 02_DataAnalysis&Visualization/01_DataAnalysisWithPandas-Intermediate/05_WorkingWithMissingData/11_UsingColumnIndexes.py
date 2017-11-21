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

# Assign the fifth row from new_titanic_survival to row_position_fifth
row_position_fifth = new_titanic_survival.iloc[4]

# Assign the row with index label 25 from new_titanic_survivalto row_index_25
row_index_25 = new_titanic_survival.loc[25]

# Assign the value at row index label 1100, column index label
# "age" from new_titanic_survival to row_index_1100_age.
row_index_1100_age = new_titanic_survival.loc[1100,'age']
print(row_index_1100_age)
raw_input("Press Enter To Continue")

# Assign the value at row index label 25, column index label
# "survived" from new_titanic_survival to row_index_25_survived.
row_index_25_survived = new_titanic_survival.loc[25, 'survived']
print(row_index_25_survived)
raw_input("Press Enter To Continue")

# Assign the first 5 rows and first three columns from new_titanic_survival to five_rows_three_cols
five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]
print(five_rows_three_cols)