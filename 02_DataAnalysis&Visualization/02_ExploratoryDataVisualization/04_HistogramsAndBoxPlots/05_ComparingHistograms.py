import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv('fandango_scores.csv')

fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(reviews['Fandango_Ratingvalue'], bins=20, range=(0, 5))
ax1.set_ylim(0, 50)
ax1.set_title('Distribution of Fandango Ratings')

ax2.hist(reviews['RT_user_norm'], bins=20, range=(0, 5))
ax2.set_ylim(0, 50)
ax2.set_title('Distribution of Rotten Tomatoes Ratings')

ax3.hist(reviews['Metacritic_user_nom'], bins=20, range=(0, 5))
ax3.set_ylim(0, 50)
ax3.set_title('Distribution of Metacritic Ratings')

ax4.hist(reviews['IMDB_norm'], bins=20, range=(0, 5))
ax4.set_ylim(0, 50)
ax4.set_title('Distribution of IMDB Ratings')

plt.show()