import matplotlib.pyplot as plt
import pandas as pd
import os



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
# Visualize the point guards
# fig = plt.figure()
plt.scatter(point_guards['ppg'], point_guards['atr'], c='y')
plt.title("Point Guards")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plot_file_name = os.path.splitext(os.path.basename(__file__))[0]+'_fig1.png'
plt.savefig(plot_file_name, bbox_inches='tight')
plt.show()
