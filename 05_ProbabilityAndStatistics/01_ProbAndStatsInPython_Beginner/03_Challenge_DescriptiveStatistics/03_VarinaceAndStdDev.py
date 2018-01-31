import matplotlib.pyplot as plt
import pandas as pd

def calc_mean(series):
    return series.mean()

def calc_variance(series):
    series_mean = calc_mean(series)
    variances = [(i - series_mean) ** 2 for i in series.values]
    return sum(variances) / len(variances)

def calc_variance_std_dev(series):
    var = calc_variance(series)
    return (var ** 0.5), var 


movie_reviews = pd.read_csv("fandango_score_comparison.csv")
user_reviews_cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']
user_reviews = movie_reviews[user_reviews_cols].copy()

rt_stdev, rt_var = calc_variance_std_dev(user_reviews[user_reviews_cols[0]])
mc_stdev, mc_var = calc_variance_std_dev(user_reviews[user_reviews_cols[1]])
fg_stdev, fg_var = calc_variance_std_dev(user_reviews[user_reviews_cols[2]])
id_stdev, id_var = calc_variance_std_dev(user_reviews[user_reviews_cols[3]])

print('rt_stdev:', rt_stdev)
print('rt_var:', rt_var)
print('mc_stdev:', mc_stdev)
print('mc_var:', mc_var)
print('fg_stdev:', fg_stdev)
print('fg_var:', fg_var)
print('id_stdev:', id_stdev)
print('id_var:', id_var)

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

ax1.set_title("RT_user_norm")
ax2.set_title("Metacritic_user_nom")
ax3.set_title("Fandango_Ratingvalue")
ax4.set_title("IMDB_norm")

plt.show()