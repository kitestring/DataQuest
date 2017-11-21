import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x_values = unrate['DATE']
y_values = unrate['VALUE']

ax1.plot(x_values.iloc[0:12], y_values.iloc[0:12])
ax1.set_title('Monthly Unemployment Rate, 1948')

ax2.plot(x_values.iloc[12:24], y_values.iloc[12:24])
ax2.set_title('Monthly Unemployment Rate, 1949')

plt.show()