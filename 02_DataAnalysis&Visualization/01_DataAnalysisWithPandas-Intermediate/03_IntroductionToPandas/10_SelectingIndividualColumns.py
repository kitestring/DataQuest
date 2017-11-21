import pandas

food_info = pandas.read_csv('food_info.csv')

saturated_fat = food_info['FA_Sat_(g)']
cholesterol = food_info['Cholestrl_(mg)']

print(saturated_fat)
print(cholesterol)