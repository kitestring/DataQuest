import pandas

food_info = pandas.read_csv('food_info.csv')

normalized_protein = food_info['Protein_(g)'] / food_info['Protein_(g)'].max()

normalized_fat = food_info['Lipid_Tot_(g)'] / food_info['Lipid_Tot_(g)'].max()