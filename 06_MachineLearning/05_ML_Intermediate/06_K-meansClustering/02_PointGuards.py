import pandas as pd

nba = pd.read_csv("nba_2013.csv")

point_guards = nba[nba['pos'] == 'PG'].copy()