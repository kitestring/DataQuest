import pandas as pd

def std_dev(data_series):
    series_mean = data_series.mean()
    variance_unsummed = [(i-series_mean) **2 for i in data_series]
    return (sum(variance_unsummed)/len(variance_unsummed)) ** 0.5

nba_stats = pd.read_csv('nba_2013.csv')

mp_dev = std_dev(nba_stats['mp'])
print(mp_dev)

ast_dev = std_dev(nba_stats['ast'])
print(ast_dev)