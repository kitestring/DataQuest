import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

# Uses the pandas data time function to convet a date into an integer corresponding to the month number
unrate['MONTH'] = unrate['DATE'].dt.month

color_codes = ['red', 'blue']

fig = plt.figure(figsize=(6, 3))

x_values = unrate['MONTH']
y_values = unrate['VALUE']

for plot in range(0,2):
	start_row = 0 + (12 * plot)
	end_row = 12 + (12 * plot)
	data_date = 1948 + plot 
	plot_number = plot + 1
	
	plt.plot(x_values.iloc[start_row:end_row], y_values.iloc[start_row:end_row], color=color_codes[plot])
	
plt.show()