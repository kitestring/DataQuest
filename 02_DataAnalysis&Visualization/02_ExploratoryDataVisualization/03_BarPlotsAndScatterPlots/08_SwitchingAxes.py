import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('fandango_scores.csv')

# The Axes.bar() method has 2 required parameters, left and height. We use the left
# parameter to specify the x coordinates of the left sides of the bar (marked in
# blue on the above image). We use the height parameter to specify the height of each
# bar. Both of these parameters accept a list-like object.
fig = plt.figure(figsize=(5, 10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

y_series_1 = reviews['Fandango_Ratingvalue']
x_series_1 = reviews['RT_user_norm']

x_series_2 = reviews['Fandango_Ratingvalue']
y_series_2 = reviews['RT_user_norm']

ax1.scatter(x_series_1, y_series_1)
ax2.scatter(x_series_2, y_series_2)

plt.show()