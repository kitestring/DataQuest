import pandas

food_info = pandas.read_csv('food_info.csv')

# Series object representing the "NDB_No" column.
ndb_col = food_info["NDB_No"]

# You can instead access a column by passing in a string variable.
col_name = "NDB_No"
ndb_col = food_info[col_name]

# Output result
print(col_name)
print(ndb_col)