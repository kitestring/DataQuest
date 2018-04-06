import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

votes = pd.read_csv('114_congress.csv')

kmeans_model = KMeans(n_clusters=2, random_state=1)
senator_distances = kmeans_model.fit_transform(votes.iloc[:,3:])

# Cube each value then sum to increase the distance and thus make the extremes more apparent to find
extremism = np.sum((senator_distances**3), axis=1)

votes['extremism'] = extremism
votes.sort_values(by='extremism', ascending=False, inplace=True)

print(votes.head(10))