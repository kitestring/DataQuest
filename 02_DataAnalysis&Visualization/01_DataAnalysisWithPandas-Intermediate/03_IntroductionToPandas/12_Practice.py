import pandas

food_info = pandas.read_csv('food_info.csv')

columns = food_info.columns
columns = columns.tolist()
gram_columns = []

for column in columns:
	if column.endswith('(g)'):
		gram_columns.append(column)
		
gram_df = food_info[gram_columns]
print(gram_df.head(3))