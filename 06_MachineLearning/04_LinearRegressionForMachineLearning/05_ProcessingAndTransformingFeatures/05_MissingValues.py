# Select only the columns from train that contain more than 0 missing values but less 
#     than 584 missing values. Assign the resulting data frame to df_missing_values.
# Display the number of missing values for each column in df_missing_values.
# Display the data type for each column in df_missing_values.

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data[0:1460].copy()
test = data[1460:].copy()

train_null_counts = train.isnull().sum()
missing_values_cols = train_null_counts[(train_null_counts > 0) & (train_null_counts < 584)].index
# ['Lot Frontage', 'Mas Vnr Type', 'Mas Vnr Area', 'Bsmt Qual',
#        'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin SF 1',
#        'BsmtFin Type 2', 'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
#        'Bsmt Full Bath', 'Bsmt Half Bath', 'Garage Type', 'Garage Yr Blt',
#        'Garage Finish', 'Garage Qual', 'Garage Cond']

df_missing_values = train[missing_values_cols]
print(df_missing_values.info())
# RangeIndex: 1460 entries, 0 to 1459
# Data columns (total 19 columns):
# Lot Frontage      1211 non-null float64
# Mas Vnr Type      1449 non-null object
# Mas Vnr Area      1449 non-null float64
# Bsmt Qual         1420 non-null object
# Bsmt Cond         1420 non-null object
# Bsmt Exposure     1419 non-null object
# BsmtFin Type 1    1420 non-null object
# BsmtFin SF 1      1459 non-null float64
# BsmtFin Type 2    1419 non-null object
# BsmtFin SF 2      1459 non-null float64
# Bsmt Unf SF       1459 non-null float64
# Total Bsmt SF     1459 non-null float64
# Bsmt Full Bath    1459 non-null float64
# Bsmt Half Bath    1459 non-null float64
# Garage Type       1386 non-null object
# Garage Yr Blt     1385 non-null float64
# Garage Finish     1385 non-null object
# Garage Qual       1385 non-null object
# Garage Cond       1385 non-null object
# dtypes: float64(9), object(10)
# memory usage: 216.8+ KB
# None