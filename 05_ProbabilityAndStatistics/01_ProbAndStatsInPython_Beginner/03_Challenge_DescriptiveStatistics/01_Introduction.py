import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

# ax1.hist(movie_reviews['RT_user_norm'])
# ax2.hist(movie_reviews['Metacritic_user_nom'])
# ax3.hist(movie_reviews['Fandango_Ratingvalue'])
# ax4.hist(movie_reviews['IMDB_norm'])

# This is an alternative way to do it, this method automatically puts gridlines on the plot
# other than that it's basically the same.
movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

ax1.set_title("RT_user_norm")
ax2.set_title("Metacritic_user_nom")
ax3.set_title("Fandango_Ratingvalue")
ax4.set_title("IMDB_norm")

plt.show()