import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors.regression import KNeighborsRegressor

# reads and cleans DataFrame
dc_listings = pd.read_csv("dc_airbnb.csv")
dc_listings.rename(columns=lambda col_header: col_header.strip(), inplace=True)
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

kf = KFold(n_splits=5, shuffle=True, random_state=1)
knn = KNeighborsRegressor()
mses = cross_val_score(estimator=knn, X=dc_listings[['accommodates']], y=dc_listings['price'], scoring="neg_mean_squared_error", cv=kf)
# mses_abs_sqrt = [x ** 0.5 for x in abs(mses)]
mses_abs_sqrt = np.sqrt(np.absolute(mses))
avg_rmse = np.mean(mses_abs_sqrt)

print('mses_abs_sqrt:', mses_abs_sqrt)
print('avg_rmse:', avg_rmse)

# mses_abs_sqrt: [ 117.38752023  137.27049219  146.0660213   106.37023494  145.75598127]
# avg_rmse: 130.570049986
