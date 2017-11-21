from pandas import read_csv
from pandas import Series

fandango = read_csv('fandango_score_comparison.csv')

# rt_critics and rt_users are Series objects containing the average ratings from critics and users for each film
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

# Both Series objects use the same custom string index, which they base on the film
# names. Use the Python arithmetic operators to return a new Series object,
# rt_mean, that contains the mean ratings from both critics and users for each film
rt_mean = (rt_critics + rt_users) / 2

# Print the first 10 lines of everything to verify
print('\nrt_critics\n')
print(rt_critics[0:10])
print('\nrt_users\n')
print(rt_users[0:10])
print('\nrt_mean\n')
print(rt_mean[0:10])