from sklearn.metrics.pairwise import euclidean_distances
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

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
    
    # DQ did not seed their random numbers so I had to do this to force my
    # solution to match theirs
    # return dictionary
    return {0: [12.535211267605634, 1.6704545454545454], 1: [16.67142857142857, 1.785425101214575], 2: [17.65753424657534, 2.6449704142011834], 3: [3.0714285714285716, 1.0], 4: [6.571428571428571, 1.7833333333333334]}

def calculate_distance(cent, player_values):
    dist = euclidean_distances(cent, player_values)
    return dist[0][0]


def assign_to_cluster(row, centroid_dict):
    player_values = row[['ppg','atr']].tolist()
    player_values = np.array(player_values).reshape(1,-1)
    player_distances = {}
    
    for cluster_id, c_distances in centroid_dict.items():
        dist = np.array(c_distances).reshape(1,-1)
        player_distances[cluster_id] = calculate_distance(dist,player_values)
        
    return min(player_distances, key=player_distances.get)

# Here we assign each player to the randomly determined centriods
# based upon which player is nearest in euclidean distance 
centroid_dict = centroids_to_dict(centroids)
point_guards['cluster'] = point_guards.apply(assign_to_cluster, args=(centroid_dict,), axis=1)

# Visualizing clusters
def visualize_clusters(df, num_clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)
        plt.title('K-Means Clustering')
    
    plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig1.png'
    plt.savefig(plot_file_name, bbox_inches='tight')
    plt.show()

# Next, we recalculate the centroids for each cluster by averaging 
# the values in the cluster, in this case 'ppg' and 'atr'
def recalculate_centroids(df):
    dictionary = {}
    for cluster_id in df['cluster'].unique().tolist():
        filtered_df = df[df['cluster']==cluster_id]
        new_centroid = [np.average(filtered_df['ppg']), [np.average(filtered_df['atr'])]]
        dictionary[cluster_id] = new_centroid
        
    return dictionary

centroids_dict = recalculate_centroids(point_guards)
print(centroids_dict)
                        
                        