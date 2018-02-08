from scipy.stats import chisquare
import numpy as np

observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

chisquare_value, race_pvalue = chisquare(observed, expected)

print('chisquare_value:', chisquare_value)
print('race_pvalue:', race_pvalue)