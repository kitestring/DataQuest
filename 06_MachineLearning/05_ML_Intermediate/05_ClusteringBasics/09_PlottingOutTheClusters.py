import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

votes = pd.read_csv('114_congress.csv')


kmeans_model = KMeans(n_clusters=2, random_state=1)

senator_distances = kmeans_model.fit_transform(votes.iloc[:,3:])

# extract the cluster labels
labels = kmeans_model.labels_

fig = plt.figure()
plt.scatter(senator_distances[:,0],senator_distances[:,1],c=labels)

plt.show()