from scipy.stats.stats import pearsonr
import pandas as pd

nba_stats = pd.read_csv('nba_2013.csv')

# The pearsonr function will find the correlation between two columns of data.
# It returns the r value and the p value.  We'll learn more about p values later on.
r, p_value = pearsonr(nba_stats["fga"], nba_stats["pts"])
# As we can see, this is a very high positive r value - it's close to 1.
print(r)

# These two columns are much less correlated.
r, p_value = pearsonr(nba_stats["trb"], nba_stats["ast"])
# We get a much lower, but still positive, r value.
print(r)

r_fta_pts, p_value_fta_pts = pearsonr(nba_stats["fta"], nba_stats["pts"])

r_stl_pf,  p_value_stl_pf = pearsonr(nba_stats["stl"], nba_stats["pf"])

print('r_fta_pts:', r_fta_pts)
print('r_stl_pf,', r_stl_pf)