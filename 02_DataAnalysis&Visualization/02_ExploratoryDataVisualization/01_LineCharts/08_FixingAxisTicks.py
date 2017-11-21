import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

# matplotlib cannot directly plot the dates because currently they are strings (objects) and must because
# converted to a date data type
unrate['DATE'] = pd.to_datetime(unrate['DATE'], format='%Y-%m-%d')

x_values = unrate['DATE']
y_values = unrate['VALUE']

plt.plot(x_values.iloc[0:12], y_values.iloc[0:12])
#plt.xticks(rotation='vertical') In this case, this basically does the same thing
plt.xticks(rotation=90)

plt.show()