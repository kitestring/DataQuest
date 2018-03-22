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
df_missing_values = train[missing_values_cols]

# Helpful tid-bits
# Only select float columns.
# missing_floats = df_missing_vals.select_dtypes(include=['float'])
# Returns a data frame with missing values replaced with 0.
# fill_with_zero = missing_floats.fillna(0)
# Returns a data frame with missing values replaced with mean of that column.
# fill_with_mean = missing_floats.fillna(missing_floats.mean())

float_cols = df_missing_values.select_dtypes(include=['float'])

float_cols = float_cols.fillna(df_missing_values.mean())
print(float_cols.isnull().sum())
# Lot Frontage      0
# Mas Vnr Area      0
# BsmtFin SF 1      0
# BsmtFin SF 2      0
# Bsmt Unf SF       0
# Total Bsmt SF     0
# Bsmt Full Bath    0
# Bsmt Half Bath    0
# Garage Yr Blt     0
# dtype: int64