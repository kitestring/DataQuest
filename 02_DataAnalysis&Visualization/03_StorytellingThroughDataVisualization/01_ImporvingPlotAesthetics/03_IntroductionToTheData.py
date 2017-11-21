# Generate a line chart that visualizes the
# historical percentage of Biology degrees awarded to women

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
     
fig, ax = plt.subplots()
     
ax.plot(women_degrees['Year'], women_degrees['Biology'])


plt.show()