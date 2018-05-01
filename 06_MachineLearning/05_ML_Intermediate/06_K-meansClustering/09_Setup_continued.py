import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

nba = pd.read_csv("nba_2013.csv")

# Buiding the point_guards df
point_guards = nba[nba['pos'] == 'PG'].copy()
# Add a points per game column
point_guards['ppg'] = point_guards['pts'] / point_guards['g']
# Add a assists/turnover ratio column, first drop the players who have 0 turnovers.
    # Not only did these players only play a few games, making it hard to understand 
    # their true abilities, but we also cannot divide by 0 when we calculate atr.
point_guards = point_guards[point_guards['tov'] != 0]
point_guards['atr'] = point_guards['ast'] / point_guards['tov']

# Setting up k-means
num_clusters = 5
# Use numpy's random function to generate a list, length: num_clusters, of indices
random_initial_points = np.random.choice(point_guards.index, size=num_clusters)
# Use the random indices to create the centroids
centroids = point_guards.loc[random_initial_points]

def centroids_to_dict(centroids):
    # Converts the centroids to a dictionary with the keys and values defined below.
        # key: cluster_id of that centroid's cluster
        # value: centroid's coordinates expressed as a list ( ppg value first, atr value second )
    dictionary = {}
    # iterating counter we use to generate a cluster_id
    counter = 0

    # iterate a pandas data frame row-wise using .iterrows()
    for index, row in centroids.iterrows():
        coordinates = [row['ppg'], row['atr']]
        dictionary[counter] = coordinates
        counter += 1

    return dictionary

centroids_dict = centroids_to_dict(centroids)
print(centroids_dict)
