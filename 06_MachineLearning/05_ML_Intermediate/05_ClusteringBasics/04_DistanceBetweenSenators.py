import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

votes = pd.read_csv('114_congress.csv')

# print(votes.iloc[0,3:].values)
# [0.0 1.0 1.0 1.0 1.0 0.0 0.0 1.0 1.0 1.0 0.0 0.0 0.0 0.0 0.0]

# print(votes.iloc[0,3:].values.reshape(1,-1))
# [[0.0 1.0 1.0 1.0 1.0 0.0 0.0 1.0 1.0 1.0 0.0 0.0 0.0 0.0 0.0]]

distance = euclidean_distances(votes.iloc[0,3:].values.reshape(1, -1), votes.iloc[2,3:].values.reshape(1, -1))
print(distance)