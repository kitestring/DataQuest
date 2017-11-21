import pandas as pd
import matplotlib.pyplot as plt

norm_reviews = pd.read_csv('fandango_scores.csv')

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']

fig, ax = plt.subplots()

ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation='vertical')
ax.set_ylim(0, 5)

plt.show()

