from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

# Read csv file and assign column names
headers=['symboling','normalized_losses','make','fuel_type','aspiration','num_of_doors',
         'body_style','drive_wheels','engine_location','wheel_base','length','width',
        'height','curb_weight','engine_type','num_of_cylinders','engine_size','fuel_system',
        'bore','stroke','compression_ratio','horsepower','peak_rpm','city_mpg','highway_mpg',
        'price']
cars = pd.read_csv('imports-85.data.txt', names=headers)

# Select only the columns with continuous values from - https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names
continuous_values_cols = ['normalized_losses', 'wheel_base', 'length', 'width', 'height', 'curb_weight', 
                          'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm', 'city_mpg', 'highway_mpg', 'price']
numeric_cars = cars[continuous_values_cols].copy()

# Clean Data Set by Convert missing values (?) with np.NaN then set the type to float
numeric_cars.replace(to_replace='?', value=np.nan, inplace=True)
numeric_cars = numeric_cars.astype('float')

# Because the column we're trying to predict is 'price', any row were price is NaN will be removed."
# print(numeric_cars.info())
numeric_cars = numeric_cars.dropna(subset=['price'])

# print('******')
# print(numeric_cars.info())

# exit()

# All remaining NaN's will be filled with the mean of its respective column
numeric_cars = numeric_cars.fillna(numeric_cars.mean())

# Create training feature list and k value list
test_features = numeric_cars.columns.tolist()
predictive_feature = 'price'
test_features.remove(predictive_feature)
k_values = [x for x in range(10) if x/2 != round(x/2)]

# Normalize columns
numeric_cars_normalized = numeric_cars[test_features].copy()
numeric_cars_normalized = numeric_cars_normalized/ numeric_cars.max()
numeric_cars_normalized[predictive_feature] = numeric_cars[predictive_feature].copy()


def knn_train_test(df, train_columns, predict_feature, k_value):
    
    # Randomly resorts the DataFrame to mitigate sampling bias
    np.random.seed(1)
    df = df.loc[np.random.permutation(len(df))]

    # Split the DataFrame into ~75% train / 25% test data sets
    split_integer = round(len(df) * 0.75)
    train_df = df.iloc[0:split_integer]
    test_df = df.iloc[split_integer:]
    
    train_features = train_df[train_columns]
    train_target = train_df[predict_feature]
    
    # Trains the model
    knn = KNeighborsRegressor(n_neighbors=k_value)
    knn.fit(train_features, train_target)
    
    # Test the model & return calculate mean square error
    predictions = knn.predict(test_df[train_columns])
    print("predictions")
    mse = mean_squared_error(y_true=test_df[predict_feature], y_pred=predictions)
    return mse



# Verify data for NaN and inf
print(len(numeric_cars_normalized))
# 201

print(numeric_cars_normalized.info())
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 201 entries, 0 to 204
# Data columns (total 14 columns):
# bore                 201 non-null float64
# city_mpg             201 non-null float64
# compression_ratio    201 non-null float64
# curb_weight          201 non-null float64
# height               201 non-null float64
# highway_mpg          201 non-null float64
# horsepower           201 non-null float64
# length               201 non-null float64
# normalized_losses    201 non-null float64
# peak_rpm             201 non-null float64
# price                201 non-null float64
# stroke               201 non-null float64
# wheel_base           201 non-null float64
# width                201 non-null float64
# dtypes: float64(14)
# memory usage: 23.6 KB
# None

print(numeric_cars_normalized.isnull().sum())
# bore                 0
# city_mpg             0
# compression_ratio    0
# curb_weight          0
# height               0
# highway_mpg          0
# horsepower           0
# length               0
# normalized_losses    0
# peak_rpm             0
# price                0
# stroke               0
# wheel_base           0
# width                0
# dtype: int64

# The loop below, essentially does the same as the above
# verification, but using different methods
# the purpose is to prove there's no nan or inf in my data set
index = []
NaN_counter = []
inf_counter = []
for col in numeric_cars_normalized.columns:
    index.append(col)
    # inf counter
    col_isinf = np.isinf(numeric_cars_normalized[col])
    if col_isinf.value_counts().index[0] == False:
        inf_counter.append(col_isinf.value_counts()[0])
    
    # nan counter    
    col_isnan = np.isnan(numeric_cars_normalized[col])
    if col_isnan.value_counts().index[0] == False:
        NaN_counter.append(col_isnan.value_counts()[0])

data_check = {'NOT_NaN_count': NaN_counter, 'NOT_inf_count': inf_counter}
data_verification = pd.DataFrame(data=data_check, index=index)
print(data_verification)

#                    NOT_NaN_count  NOT_inf_count
# bore                         201            201
# city_mpg                     201            201
# compression_ratio            201            201
# curb_weight                  201            201
# height                       201            201
# highway_mpg                  201            201
# horsepower                   201            201
# length                       201            201
# normalized_losses            201            201
# peak_rpm                     201            201
# price                        201            201
# stroke                       201            201
# wheel_base                   201            201
# width                        201            201
# instantiate mse dict
mse_dict = {}


# Here's a another methodology for extra redudnant data checking
index = []
NaN_counter = []
inf_counter = []

for col in numeric_cars_normalized.columns:
    index.append(col)
    inf_counter.append(np.any(np.isfinite(numeric_cars_normalized[col])))
    NaN_counter.append(np.any(np.isnan(numeric_cars_normalized[col])))
 
data_check = {'Any_NaN': NaN_counter, 'Any_inf': inf_counter}
data_verification = pd.DataFrame(data=data_check, index=index)
print(data_verification)

#                    Any_NaN  Any_inf
# bore                 False     True
# city_mpg             False     True
# compression_ratio    False     True
# curb_weight          False     True
# height               False     True
# highway_mpg          False     True
# horsepower           False     True
# length               False     True
# normalized_losses    False     True
# peak_rpm             False     True
# price                False     True
# stroke               False     True
# wheel_base           False     True
# width                False     True

# test each feature and do so with a range of k values
# in an effort to determine the optimal training feature and k value
for feature in test_features:
 
    mse = [knn_train_test(numeric_cars_normalized,feature, predictive_feature, k) for k in k_values]
    mse_dict[feature] = mse
     
print(mse_dict)

