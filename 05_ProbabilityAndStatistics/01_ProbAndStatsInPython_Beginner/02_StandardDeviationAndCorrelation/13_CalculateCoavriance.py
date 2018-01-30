from scipy.stats.stats import pearsonr
import pandas as pd

nba_stats = pd.read_csv('nba_2013.csv')

def co_var(x_series, y_series):
    if len(x_series) == len(y_series):
        mean_x = x_series.mean()
        mean_y = y_series.mean()
        variances_x = [i - mean_x for i in x_series]
        variances_y = [i - mean_y for i in y_series]
        variances_xy_product = [variances_x[i] * variances_y[i] for i in range(len(x_series))]
        return sum(variances_xy_product)/len(x_series)
    else:
        raise ValueError('The provided data series do not have the same number of elements')
    
cov_stl_pf = co_var(nba_stats['stl'], nba_stats['pf'])
cov_fta_pts = co_var(nba_stats['fta'], nba_stats['pts'])

print('cov_fta_pts:', cov_fta_pts)
print('cov_stl_pf:', cov_stl_pf)
