import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

x_values = unrate['DATE']
y_values = unrate['VALUE']

plt.plot(x_values.iloc[0:12], y_values.iloc[0:12])
plt.plot(x_values.iloc[12:24], y_values.iloc[12:24])

plt.show()