import pandas

food_info = pandas.read_csv('food_info.csv')

last_row = food_info.shape[0]
fifth_to_last_row = last_row - 5
last_rows = food_info.loc[fifth_to_last_row:last_row]

print(last_rows)