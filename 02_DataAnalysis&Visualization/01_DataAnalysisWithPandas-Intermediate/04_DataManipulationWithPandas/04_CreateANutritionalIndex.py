import pandas

food_info = pandas.read_csv('food_info.csv')

initial_rating = (food_info['Protein_(g)'] * 2) - (food_info['Lipid_Tot_(g)'] * 0.75)