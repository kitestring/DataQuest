import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

# matplotlib cannot directly plot the dates because currently they are strings (objects) and must because
# converted to a date data type
unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

x_values = unrate['DATE']
y_values = unrate['VALUE']

# This makes the plot and defines the x & y values
plt.plot(x_values.iloc[0:12], y_values.iloc[0:12])

# This rotates the x axis values
#plt.xticks(rotation='vertical') In this case, this basically does the same thing
plt.xticks(rotation=90)

# This adds a titles to the plot, x-axis, and y-axis
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.show()