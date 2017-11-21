import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv('fandango_scores.csv')

desired_cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

norm_reviews = reviews[desired_cols]

# The Axes.bar() method has 2 required parameters, left and height. We use the left
# parameter to specify the x coordinates of the left sides of the bar (marked in
# blue on the above image). We use the height parameter to specify the height of each
# bar. Both of these parameters accept a list-like object.
fig, ax = plt.subplots()

# Lables on the left side of the chart (axis object)
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

# Values that correspond to each label
bar_heights = norm_reviews[num_cols].iloc[0].values

# Positions of the left sides of the 5 bars. [0.75, 1.75, 2.75, 3.75, 4.75]
bar_positions = arange(5) + 0.75

# We can also use the width parameter to specify the width of each bar. This is an
# optional parameter and the width of each bar is set to 0.8 by default. The following
# code sets the width parameter to 0.5
ax.bar(bar_positions, bar_heights, 0.5)

# Adding labels and titles
tick_positions = range(1,6)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_xlabel('Rating Source')
ax.set_ylabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')

plt.show()

