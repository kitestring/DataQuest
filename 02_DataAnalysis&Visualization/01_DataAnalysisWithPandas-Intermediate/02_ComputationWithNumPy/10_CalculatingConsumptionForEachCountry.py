import numpy as np

world_alcohol = np.array(np.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=1, dtype='U75'))

# note, it really bothers me that we're not doing this for every year

# Create totals dictionary
totals = {}

# Get vector that contains a unique list of all years
years = world_alcohol[:,0]
years = np.unique(years)

# Define which year we'll extract data for...
year = '1989'

# Get a vector that contains a unique list of all the countries
countries = world_alcohol[:,2]
countries = np.unique(countries)

# Loop through a list of countries
for country in countries:
	
	# Select only the rows from year that match the given country & extract the fifth column 
	is_country_consumption = (world_alcohol[:,0] == year) & (world_alcohol[:,2] == country)
	country_consumption = world_alcohol[is_country_consumption,4]
	
	# Replace any empty string values in the vector with the '0'
	is_value_empty = country_consumption == ''
	country_consumption[is_value_empty] = '0'
	
	# Convert the vector to the float data type
	country_consumption = country_consumption.astype(float)
	
	# sum of the vector
	sum_country_consumption = country_consumption.sum()
	
	# Add the sum to the totals dictionary, with the country name as the key
	totals[country] = sum_country_consumption
	
	# Print the country & sum to the concole
	print('%s:  %f' % (country, sum_country_consumption))

