import pandas as pd
import time
start_time = time.time()


data = pd.read_csv('thanksgiving-2015-poll-data.csv', encoding="Latin-1")
regions = data['US Region'].value_counts().keys()
main_dish = data['What is typically the main dish at your Thanksgiving dinner?']
main_dish_prep = data['How is the main dish typically cooked?']
regional_entire_meal_data_rows = []

for region in regions:
	is_in_region = data['US Region'] == region
	most_common_regional_dish = main_dish[is_in_region].value_counts().keys().tolist()[0]
	is_region_and_most_common_dish = (is_in_region) & (main_dish == most_common_regional_dish)
	most_common_regional_dish_prep_type = main_dish_prep[is_region_and_most_common_dish].value_counts().keys().tolist()[0]
	regional_entire_meal_data_rows.append((region, most_common_regional_dish, most_common_regional_dish_prep_type))
	
labels = ['US Region', 'Most Common Main Dish', 'Most Common Prep Type for Main Dish']
regional_main_dish_data = pd.DataFrame(regional_entire_meal_data_rows, columns=labels)

full_meal_message = '''\n\nThe table below shows a breakdown of the most common 
full Thanksgiving meal broken down by region.\n'''
print(full_meal_message)
print(regional_main_dish_data)

print("--- %s seconds ---" % (time.time() - start_time))