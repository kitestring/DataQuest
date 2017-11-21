import pandas

food_info = pandas.read_csv('food_info.csv')

hundredth_row = food_info.loc[99]

print(hundredth_row)