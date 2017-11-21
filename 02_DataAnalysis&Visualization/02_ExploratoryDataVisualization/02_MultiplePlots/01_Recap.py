import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

x_values = unrate['DATE'].iloc[0:12]
y_values = unrate['VALUE'].iloc[0:12]

plt.plot(x_values, y_values)

plt.xticks(rotation='vertical')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.show()