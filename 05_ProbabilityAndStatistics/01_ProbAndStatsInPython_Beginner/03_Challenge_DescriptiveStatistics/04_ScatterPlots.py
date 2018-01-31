import matplotlib.pyplot as plt
import pandas as pd

movie_reviews = pd.read_csv("fandango_score_comparison.csv")
user_reviews_cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']
user_reviews = movie_reviews[user_reviews_cols].copy()

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(user_reviews[user_reviews_cols[0]], user_reviews[user_reviews_cols[2]])
ax2.scatter(user_reviews[user_reviews_cols[1]], user_reviews[user_reviews_cols[2]])
ax3.scatter(user_reviews[user_reviews_cols[3]], user_reviews[user_reviews_cols[2]])

ax1.set_xlim(0,5)
ax2.set_xlim(0,5)
ax3.set_xlim(0,5)

ax1.set_title('Fandango user reviews vs. Rotten Tomatoes user reviews')
ax2.set_title('Fandango user reviews vs. Metacritic user reviews')
ax3.set_title('Fandango user reviews vs. IMDB user reviews')


plt.show()