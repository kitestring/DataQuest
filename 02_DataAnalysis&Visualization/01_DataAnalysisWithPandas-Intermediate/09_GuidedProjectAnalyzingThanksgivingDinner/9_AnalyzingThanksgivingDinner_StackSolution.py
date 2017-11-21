import pandas as pd
import time
start_time = time.time()

data = pd.read_csv('thanksgiving-2015-poll-data.csv', encoding="Latin-1")

columns = data.keys()

region_col = 'US Region'
main_dish_col = 'What is typically the main dish at your Thanksgiving dinner?'
main_dish_prep_col = 'How is the main dish typically cooked?'
desired_cols = [region_col, main_dish_col, main_dish_prep_col]

sides_columns = [region_col]
for column in columns:
	if 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply.' in column:
		sides_columns.append(column)

sides_data = data[sides_columns]


regional_entire_meal_data_rows  = []

for region, dish_group in data[desired_cols].groupby(region_col):
	main_dish = dish_group[main_dish_col]
	main_dish_prep = dish_group[main_dish_prep_col]
	
	most_common_dish = main_dish.value_counts().index[0]
	prep_types = main_dish_prep[main_dish == most_common_dish]
	most_common_prep_type = prep_types.value_counts().index[0]
	
	
	regional_sides = []
	regional_sides_counts = []
	
	for sides_column in sides_columns[1:]:
		side_series = sides_data[sides_column]
		regional_sides_series = side_series[sides_data[region_col] == region]
		regional_sides.append(regional_sides_series.value_counts().index[0])
		regional_sides_counts.append(regional_sides_series.value_counts()[0])
	
	side_counts_series = pd.Series(data=regional_sides_counts, index=regional_sides)
	side_counts_series.sort_values(ascending=False, inplace=True)
	
	regional_entire_meal_data_rows.append((region, most_common_dish, most_common_prep_type, side_counts_series.index[0], side_counts_series.index[1], side_counts_series.index[2]))
	
labels = ['US Region', 'Most Common Main Dish', 'Most Common Prep Type for Main Dish', 'Most Common Side', '2nd Most Common Side', '3rd Most Common Side']
regional_main_dish_data = pd.DataFrame(regional_entire_meal_data_rows, columns=labels)

#Provide a report for the data printed above
full_meal_message = '''\n\nThe table below shows a breakdown of the most common 
full Thanksgiving meal broken down by region.\n'''
print(full_meal_message )
print(regional_main_dish_data)