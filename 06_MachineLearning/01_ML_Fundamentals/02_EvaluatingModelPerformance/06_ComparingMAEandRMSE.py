import pandas as pd
import numpy as np

errors_one = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10])
errors_two = pd.Series([5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 1000])

mae_one = errors_one.sum() / len(errors_one)
mae_two = errors_two.sum() / len(errors_two)

rmse_one = np.sqrt((errors_one**2).sum()/len(errors_one))
rmse_two = np.sqrt((errors_two**2).sum()/len(errors_two))

print('mae_one:', mae_one)
print('rmse_one:', rmse_one)
print('')
print('mae_two:', mae_two)
print('rmse_two:', rmse_two)