import pandas as pd
import numpy as np

data = pd.read_csv('thanksgiving-2015-poll-data.csv', encoding="Latin-1")

intro_message = '''Using the data set described below the following
pieces of information willbe determined:

\t1* What is the top 3 desserts & pies people eat at thanksgiving
\t2* The most common complete meal people eat
\t3* How many people worked on Black Friday
\t4* Regional patterns in the dinner menus
\t5* Age, gender, and income based patterns in dinner menus'''


data_source_description_message  = '''The dataset  stored in the "thanksgiving-2015-poll-data.csv" file. It contains 
1058 responses to an online survey about what Americans eat for Thanksgiving 
dinner. Each survey respondent was asked questions about what they typically eat 
for Thanksgiving, along with some demographic questions, like their gender, income, 
and location. This dataset will allow us to discover regional and income-based 
patterns in what Americans eat for Thanksgiving dinner.'''

print("\n\n%s\n\n\n%s" % (intro_message, data_source_description_message))


# Data Challenge #1 - What is the top 3 desserts & pies people eat at thanksgiving
pie_index = []
pie_values = []
dessert_index = []
dessert_values = []

total_responses = data.shape[0]
columns = data.keys()

# For each pie and dessert get the count and name and add each to a seperate list
# This will also grab the max value for the "other" columns
for column_header in columns:
	if 'Which type of pie is typically served at your Thanksgiving dinner?' in column_header:
		pie_value_counts = data[column_header].value_counts()
		pie_index.append(pie_value_counts.keys().tolist()[0])
		pie_values.append(pie_value_counts.values.tolist()[0])
		
	elif 'Which of these desserts do you typically have at Thanksgiving dinner?' in column_header:
		dessert_value_counts = data[column_header].value_counts()
		dessert_index.append(dessert_value_counts.keys().tolist()[0])
		dessert_values.append(dessert_value_counts.values.tolist()[0])

# Use index and values lists to make a pandas series object
# for both pies and desserts
pie_counts = pd.Series(data=pie_values, index = pie_index)
dessert_counts = pd.Series(data=dessert_values, index=dessert_index)

# Sort the series in descending order by value
pie_counts.sort_values(ascending=False, inplace=True)
dessert_counts.sort_values(ascending=False, inplace=True)

# Calculate the total percentage of people serveyed and assign it to a new pandas series object
pie_percentages = (pie_counts / total_responses) * 100
dessert_percentages = (dessert_counts / total_responses ) * 100

# Use the index and two series to make a new data frame for both pies & desserts
# Only do so using the first three rows
pie_data = pd.DataFrame()
pie_data['Pie Count'] = pie_counts.iloc[0:3]
pie_data['Pie %'] = pie_percentages.iloc[0:3]

dessert_data = pd.DataFrame()
dessert_data['Dessert Count'] = dessert_counts.iloc[0:3]
dessert_data['Dessert %'] = dessert_percentages.iloc[0:3]


# Report your pie & dessert findings
pie_message = '''\n\nThe table below shows a breakdown of the top three pies served at Thanksgiving
as well as the corresponding percentage based upon the number of respondents to this survey.\n'''
print(pie_message)
print(pie_data)

dessert_message = '''\n\nThe table below shows a breakdown of the top three desserts served at Thanksgiving
as well as the corresponding percentage based upon the number of respondents to this survey.\n'''
print(dessert_message)
print(dessert_data)


# Data Challenge #2 - What is the most common complete meal people eat

'''Skip this for now, I need some help here'''

# Data Challenge #3 - How many people worked on Black Friday?

# Create two pandas Series objects, one with the count of the black friday column in data 
# The second convert to a percentage of the todal respondents
worked_black_friday_count = data['Will you employer make you work on Black Friday?'].value_counts()
worked_black_friday_percentage = (worked_black_friday_count / total_responses) * 100

# Use the previous two pandas Series to create a new data frame
worked_black_friday = pd.DataFrame()
worked_black_friday['Worked Black Friday'] = worked_black_friday_count
worked_black_friday['Worked Black Friday %'] = worked_black_friday_percentage

# Report the black friday working data
Blk_Fri_message = '''\n\n
The table belows shows a breakdown of the number of people who have to work on black 
friday with the corresponding percentage based upon the number of respondents to this survey.\n'''
print(Blk_Fri_message)
print(worked_black_friday)

# Data Challenge #4 - Regional patterns in the dinner menus
'''Ok, for this one, lets figure out what the most common main dish and the most common method of preparation
and the top three sides.  This will be done for each region.'''

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
	# Create a series objects that contain the main dishes & main dish preparation method 
	# from the dish_group DataFrame which only contains
	# Data from the region within the current iteration
	main_dish = dish_group[main_dish_col]
	main_dish_prep = dish_group[main_dish_prep_col]
	
	# Grab the most common dish from the main_dish series object
	most_common_dish = main_dish.value_counts().index[0]
	
	# Filter the main_dish_prep object for the most common dish
	prep_types = main_dish_prep[main_dish == most_common_dish]
	
	# Grab the most common dish prep of the most common dish
	most_common_prep_type = prep_types.value_counts().index[0]
	
	
	# create the sides list that will be used to create the sides Series object
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


#  Data Challenge # - Age, gender, and income based patterns in dinner menus

age_col = 'Age'
gender_col = 'What is your gender?'
income_col = 'How much total combined money did all members of your HOUSEHOLD earn last year?'
desired_cols = [age_col, gender_col, income_col, main_dish_col, main_dish_prep_col]
demographics_labels = ['Age', 'Gender', 'Income']

sides_columns.remove(region_col)
sides_columns.insert(0, income_col)
sides_columns.insert(0, gender_col)
sides_columns.insert(0, age_col)
sides_data = data[sides_columns]

demographic_data = []

for demographic_index, deomgraphic_column in enumerate(desired_cols[0:3]):
	
	demographic_entire_meal_data_rows = []
	
	for demographic, demographic_group in data[desired_cols].groupby(deomgraphic_column):
		
		# Create a series objects that contain the main dishes & main dish preparation method 
		# from the demographic_group DataFrame which only contains
		# Data from the demographic within the current iteration
		main_dish = demographic_group[main_dish_col]
		main_dish_prep = demographic_group[main_dish_prep_col]

		# Grab the most common dish from the main_dish series object
		most_common_dish = main_dish.value_counts().index[0]
		
		# Filter the main_dish_prep series object for the most_common_dish
		prep_types = main_dish_prep[main_dish == most_common_dish]
		
		# Grab the most common prep type used for the most common dish
		most_common_prep_type = prep_types.value_counts().index[0]

		# create the sides list that will be used to create the sides Series object
		demographic_sides = []
		demographic_sides_counts = []
		
		# Iterate through each side and get the most common one for the current demographic
		for sides_column in sides_columns[3:]:
			side_series = sides_data[sides_column]
			demographic_sides_series = side_series[sides_data[deomgraphic_column] == demographic]
			demographic_sides.append(demographic_sides_series.value_counts().index[0])
			demographic_sides_counts.append(demographic_sides_series.value_counts()[0])
		
		demographic_counts_series = pd.Series(data=demographic_sides_counts, index=demographic_sides)
		demographic_counts_series.sort_values(ascending=False, inplace=True)
		
		demographic_entire_meal_data_rows.append((demographic, most_common_dish, most_common_prep_type, demographic_counts_series.index[0], demographic_counts_series.index[1], demographic_counts_series.index[2]))
		
		
		
		
		#regional_entire_meal_data_rows.append((demographic, most_common_dish, most_common_prep_type))
		

	
	# Create a DataFrame which contains the full meal break down for the given demographic
	# Then append it to the demographic_data list
	labels = [demographics_labels[demographic_index], 'Most Common Main Dish', 'Most Common Prep Type for Main Dish', 'Most Common Side', '2nd Most Common Side', '3rd Most Common Side']
	#labels = [demographics_labels[demographic_index], 'Most Common Main Dish', 'Most Common Prep Type for Main Dish']
	demographic_main_dish_data = pd.DataFrame(demographic_entire_meal_data_rows, columns=labels)
	demographic_data.append(demographic_main_dish_data)
	
	
	#Provide a report for the data printed above
	full_meal_message = '''\n\nThe table below shows a breakdown of the most common 
full Thanksgiving meal broken down by %s.\n''' % demographics_labels[demographic_index]
	print(full_meal_message )
	print(demographic_main_dish_data)



























