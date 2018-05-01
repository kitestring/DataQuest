import pandas as pd

nba = pd.read_csv("nba_2013.csv")

point_guards = nba[nba['pos'] == 'PG'].copy()
point_guards['ppg'] = point_guards['pts'] / point_guards['g']

print(point_guards[['pts', 'g', 'ppg']].head(5))