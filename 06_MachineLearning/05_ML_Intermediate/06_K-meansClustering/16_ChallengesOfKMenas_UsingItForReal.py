import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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


# Visualizing clusters
def visualize_clusters(df, num_clusters, title, figure_no):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)
        plt.title(title)
    
    plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig'+ figure_no +'.png'
    plt.savefig(plot_file_name, bbox_inches='tight')
    plt.show()

# Using sklearn to do all the crap I just did manually
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters, "K-Means Clustering with Sklearn",'1')