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

def calc_covariance(series_one, series_two):
    mean_series_one = series_one.mean()
    mean_series_two = series_two.mean()
    variances = [(series_one[i] - mean_series_one) * (series_two[i] - mean_series_two) for i in range(len(series_one))]
    return sum(variances) / len(variances)

def calc_correlation(series_one, series_two):
    covariance = calc_covariance(series_one, series_two)
    std_dev = (calc_variance(series_one) * calc_variance(series_two)) ** (0.5)
    return covariance / std_dev

movie_reviews = pd.read_csv("fandango_score_comparison.csv")
user_reviews_cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']
user_reviews = movie_reviews[user_reviews_cols].copy()

rt_fg_corr = calc_correlation(user_reviews['RT_user_norm'], user_reviews['Fandango_Ratingvalue'])
mc_fg_corr = calc_correlation(user_reviews['Metacritic_user_nom'], user_reviews['Fandango_Ratingvalue'])
id_fg_corr = calc_correlation(user_reviews['IMDB_norm'], user_reviews['Fandango_Ratingvalue'])

print('rt_fg_corr:', rt_fg_corr)
print('mc_fg_corr:', mc_fg_corr)
print('id_fg_corr:', id_fg_corr)

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