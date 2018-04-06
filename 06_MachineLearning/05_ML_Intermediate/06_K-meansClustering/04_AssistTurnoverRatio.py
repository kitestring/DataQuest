import pandas as pd

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

print(point_guards[['pts', 'g', 'ppg', 'ast', 'tov', 'atr']].head(5))
