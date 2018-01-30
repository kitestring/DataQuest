from scipy.stats.stats import pearsonr
import pandas as pd

nba_stats = pd.read_csv('nba_2013.csv')

# My attempt

# def r_value(x_series, y_series):
#     if len(x_series) == len(y_series):
#         mean_x = x_series.mean()
#         mean_y = y_series.mean()
#         std_dev_x = x_series.std()
#         std_dev_y = y_series.std()
#         variances_x = [i - mean_x for i in x_series]
#         variances_y = [i - mean_y for i in y_series]
#         variances_xy_product = [variances_x[i] * variances_y[i] for i in range(len(x_series))]
#         co_var = sum(variances_xy_product)/len(x_series)
#         return co_var / (std_dev_x * std_dev_y)
#     else:
#         raise ValueError('The provided data series do not have the same number of elements')
#     
# 
# r_fta_blk = r_value(nba_stats['fta'], nba_stats['blk'])
# r_ast_stl = r_value(nba_stats['ast'], nba_stats['stl'])
# 
# print('r_fta_blk:', r_fta_blk)
# print('r_ast_stl:', r_ast_stl)



from numpy import cov
# We've already loaded the nba_stats variable for you.
r_fta_blk = cov(nba_stats["fta"], nba_stats["blk"])[0,1] / ((nba_stats["fta"].var() * nba_stats["blk"].var())** (1/2))
r_ast_stl = cov(nba_stats["ast"], nba_stats["stl"])[0,1] / ((nba_stats["ast"].var() * nba_stats["stl"].var())** (1/2))

print('r_fta_blk:', r_fta_blk)
print('r_ast_stl:', r_ast_stl)