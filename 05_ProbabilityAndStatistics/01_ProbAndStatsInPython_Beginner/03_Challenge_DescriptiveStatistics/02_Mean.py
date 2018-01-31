import pandas as pd

def calc_mean(series):
    return series.mean()

movie_reviews = pd.read_csv("fandango_score_comparison.csv")
user_reviews_cols = ['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']
user_reviews = movie_reviews[user_reviews_cols].copy()

user_reviews_means = user_reviews.apply(calc_mean)

rt_mean = user_reviews_means['RT_user_norm']
mc_mean = user_reviews_means['Metacritic_user_nom']
fg_mean = user_reviews_means['Fandango_Ratingvalue']
id_mean = user_reviews_means['IMDB_norm']

print('rt_mean:', rt_mean)
print('mc_mean:', mc_mean)
print('fg_mean:', fg_mean)
print('id_mean:', id_mean)
