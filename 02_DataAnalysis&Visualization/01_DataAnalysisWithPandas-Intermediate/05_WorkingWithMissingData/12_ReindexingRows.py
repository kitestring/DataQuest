import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

# Drop all columns in titanic_survival that have missing values and assign the result to drop_na_columns.
drop_na_columns = titanic_survival.dropna(axis=1, how='any')

# Drop all rows in titanic_survival where the columns "age" or "sex" 
# have missing values and assign the result to new_titanic_survival.
new_titanic_survival = titanic_survival.dropna(axis=0, subset=['age', 'sex'], how='any')

# Sort the new_titanic_survival DataForm by age
new_titanic_survival = new_titanic_survival.sort_values('age', ascending=False)

# Assign the first 5 rows and first three columns from new_titanic_survival to five_rows_three_cols
five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]
print(five_rows_three_cols)

# Reindex the new_titanic_survival dataframe so the row indexes start from 0, and the old index is dropped.
new_titanic_survival.reset_index(drop=True)

# Assign the final result to titanic_reindexed.
titanic_reindexed = new_titanic_survival

# Print the first 5 rows and the first 3 columns of titanic_reindexed
print(titanic_reindexed.iloc[0:5,0:3])