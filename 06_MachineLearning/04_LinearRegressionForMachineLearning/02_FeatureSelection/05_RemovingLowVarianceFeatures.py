import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

# Selects/excludes columns based upon their dtypes. Super handy, I did this manually in the last chapter :(
numerical_train = train.select_dtypes(include=['int64', 'float64'])
# Drop the following columns that either have any missing values or need to be transformed to be useful
cols_to_drop = ['PID','Year Built','Year Remod/Add','Garage Yr Blt','Mo Sold','Yr Sold']
numerical_train = numerical_train.drop(cols_to_drop, axis=1)
# Create a Series object where the index is made up of column names and the associated values are the number of missing values
null_series = pd.Series(numerical_train.isnull().sum())
# keep only the columns with no missing values, and assign the resulting Series object to full_cols_series
full_cols_series = null_series[null_series==0]

features  = ['Wood Deck SF', 'Open Porch SF', 'Fireplaces', 'Full Bath',
       '1st Flr SF', 'Garage Area', 'Gr Liv Area', 'Overall Qual']


unit_train = (train[features] - train[features].min()) / (train[features].max() - train[features].min())


print('Rescaling Check\n\nMax Values')
print(unit_train.max())

print('\n\nMin Values')
print(unit_train.min())

sorted_vars = unit_train.var().sort_values()
print('\n\nSorted Variance Values')
print(sorted_vars)

print('\n\nFeatures with a variance > 0.015')
features  = ['Wood Deck SF', 'Fireplaces', 'Full Bath',
       '1st Flr SF', 'Garage Area', 'Gr Liv Area', 'Overall Qual']
print(features)