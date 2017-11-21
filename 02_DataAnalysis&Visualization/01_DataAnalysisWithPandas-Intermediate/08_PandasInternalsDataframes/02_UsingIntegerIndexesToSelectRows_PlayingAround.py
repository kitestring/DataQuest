import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

fandango_IMDB_sorted = fandango.sort_values('IMDB')

# print(fandango.iloc[fandango.shape[0]-1])

# print('\nSpacer\n')
# x = fandango[:1]
# print(x)
# print('\nSpacer\n')
# print(x.values)
# print(type(x))


print('\nfandango.head(5)\n')
print(fandango.head(5))
print('\nfandango_IMDB_sorted.head(5)\n')
print(fandango_IMDB_sorted.head(5))

print('\nffandango_IMDB_sorted[0:5]\n')
print(fandango_IMDB_sorted[0:5])

print('\nfandango_IMDB_sorted.iloc[0:5]\n')
print(fandango_IMDB_sorted.iloc[0:5])

