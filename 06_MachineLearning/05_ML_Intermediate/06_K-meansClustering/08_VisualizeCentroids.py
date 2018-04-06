import os
import matplotlib.pyplot as plt
import pandas as pd
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
print('random_initial_points\n')
print(random_initial_points)
# Use the random indices to create the centroids
centroids = point_guards.loc[random_initial_points]
print('\nCentroids')
print(centroids)

# Visualize the centroids so we can see where the randomly chosen centroids started out.
plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow',label='All Point Guards')
plt.scatter(centroids['ppg'], centroids['atr'], c='red',label='Randomnly Selected Centroids')
plt.title("Centroids\nNot Seeded")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.legend()
plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig1.png'
plt.savefig(plot_file_name, bbox_inches='tight')
plt.show()
