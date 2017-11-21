import pandas

food_info = pandas.read_csv('food_info.csv')

grams_of_protein_per_gram_of_water = food_info['Protein_(g)'] / food_info['Water_(g)']
print(grams_of_protein_per_gram_of_water)

milligrams_of_calcium_and_iron = food_info['Calcium_(mg)'] + food_info['Iron_(mg)']
print(milligrams_of_calcium_and_iron)
print(milligrams_of_calcium_and_iron[0:5])