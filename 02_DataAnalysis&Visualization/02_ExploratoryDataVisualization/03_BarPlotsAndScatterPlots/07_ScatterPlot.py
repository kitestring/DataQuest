import pandas as pd
import matplotlib.pyplot as plt


reviews = pd.read_csv('fandango_scores.csv')

# The Axes.bar() method has 2 required parameters, left and height. We use the left
# parameter to specify the x coordinates of the left sides of the bar (marked in
# blue on the above image). We use the height parameter to specify the height of each
# bar. Both of these parameters accept a list-like object.
fig, ax = plt.subplots()

x_series = reviews['Fandango_Ratingvalue']
y_series = reviews['RT_user_norm']

ax.scatter(x_series, y_series)

ax.set_ylabel('Rotten Tomatoes')
ax.set_xlabel('Fandango')

plt.show()