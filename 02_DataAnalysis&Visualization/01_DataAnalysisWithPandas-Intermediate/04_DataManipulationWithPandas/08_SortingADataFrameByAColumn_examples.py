import pandas

food_info = pandas.read_csv('food_info.csv')

normalized_protein = food_info['Protein_(g)'] / food_info['Protein_(g)'].max()
food_info['Normalized_Protein'] = normalized_protein

normalized_fat = food_info['Lipid_Tot_(g)'] / food_info['Lipid_Tot_(g)'].max()
food_info['Normalized_Fat'] = normalized_fat

food_info['Norm_Nutr_Index'] = (food_info['Normalized_Protein'] * 2) - (food_info['Normalized_Fat'] * 0.75)

# Sorts the DataFrame in-place, rather than returning a new DataFrame.
food_info.sort_values("Sodium_(mg)", inplace=True)

# Sorts by descending order, rather than ascending.
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)