import pandas

food_info = pandas.read_csv('food_info.csv')
col_names = food_info.columns.tolist()

print(col_names)

print(food_info.head(3))

# I'm guessing we'll be using this later?!
def calculateScore(protein, lipid):
	return (2 * protein) - (0.75 * lipid)