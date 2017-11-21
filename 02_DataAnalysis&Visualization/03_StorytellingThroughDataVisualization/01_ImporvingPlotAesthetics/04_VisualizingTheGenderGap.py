# Generate 2 line charts on the same figure:
# 1) Visualizes the percentages of Biology degrees awarded to women over time
# 2) Visualizes the percentages of Biology degrees awarded to men over time.

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
     
fig, ax = plt.subplots()
     
ax.plot(women_degrees['Year'], women_degrees['Biology'], color='blue', label='Women')
ax.plot(women_degrees['Year'], 100 - women_degrees['Biology'], color='green', label='Men')

ax.legend(['Women', 'Men'], loc="upper right")
ax.set_title("Percentage of Biology Degrees Awarded By Gender")
# ax.set_xlabel("Year")
# ax.set_ylabel("Percentage")

plt.show()