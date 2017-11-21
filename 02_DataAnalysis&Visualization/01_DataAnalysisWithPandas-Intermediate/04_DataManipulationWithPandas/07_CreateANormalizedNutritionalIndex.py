import pandas

food_info = pandas.read_csv('food_info.csv')

normalized_protein = food_info['Protein_(g)'] / food_info['Protein_(g)'].max()
food_info['Normalized_Protein'] = normalized_protein

normalized_fat = food_info['Lipid_Tot_(g)'] / food_info['Lipid_Tot_(g)'].max()
food_info['Normalized_Fat'] = normalized_fat

food_info['Norm_Nutr_Index'] = (food_info['Normalized_Protein'] * 2) - (food_info['Normalized_Fat'] * 0.75)