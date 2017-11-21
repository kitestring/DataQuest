import pandas as pd
import matplotlib.pyplot as plt

norm_reviews = pd.read_csv('fandango_scores.csv')

fig, ax = plt.subplots()

ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_xticklabels(['Rotten Tomatoes'])
ax.set_ylim(0, 5)

plt.show()