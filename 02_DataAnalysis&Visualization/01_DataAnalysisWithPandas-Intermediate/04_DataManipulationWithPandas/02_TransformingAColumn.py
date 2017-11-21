import pandas

food_info = pandas.read_csv('food_info.csv')

print(food_info['Sodium_(mg)'])
sodium_grams = food_info['Sodium_(mg)'] / 1000

print('\nConverted to grams')
print(sodium_grams)
print()

print(food_info['Sugar_Tot_(g)'])
sugar_milligrams = food_info['Sugar_Tot_(g)'] * 1000
print('\nConverted to milligrams')
print(sugar_milligrams)