# To improve the data-ink ratio, let's make the 
# following changes to the plot we created in the last step:
    # 1) Remove all of the axis tick marks.
    # 2) Hide the spines, which are the lines that 
    #    connects the tick marks, on each axis.

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

ax.tick_params(bottom="off", left="off", right="off", top="off")

ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

plt.show()