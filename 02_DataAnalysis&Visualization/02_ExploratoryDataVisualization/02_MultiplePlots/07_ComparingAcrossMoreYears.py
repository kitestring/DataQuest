import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

fig = plt.figure(figsize=(12, 12))

x_values = unrate['DATE']
y_values = unrate['VALUE']
ax_list = []

for plot in range(0,5):
	start_row = 0 + (12 * plot)
	end_row = 12 + (12 * plot)
	data_date = 1948 + plot 
	plot_number = plot + 1
	
	ax_list.append(fig.add_subplot(3,2, plot_number)) 
	ax_list[plot].plot(x_values.iloc[start_row:end_row], y_values.iloc[start_row:end_row])
	ax_list[plot].set_title('Monthly Unemployment Rate, %d' % data_date)

plt.show()