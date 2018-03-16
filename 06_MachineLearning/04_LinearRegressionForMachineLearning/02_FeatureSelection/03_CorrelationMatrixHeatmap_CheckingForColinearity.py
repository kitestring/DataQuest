import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]
target = 'SalePrice'

# Selects/excludes columns based upon their dtypes. Super handy, I did this manually in the last chapter :(
numerical_train = train.select_dtypes(include=['int64', 'float64'])
# Drop the following columns that either have any missing values or need to be transformed to be useful
cols_to_drop = ['PID','Year Built','Year Remod/Add','Garage Yr Blt','Mo Sold','Yr Sold']
numerical_train = numerical_train.drop(cols_to_drop, axis=1)
# Create a Series object where the index is made up of column names and the associated values are the number of missing values
null_series = pd.Series(numerical_train.isnull().sum())
# keep only the columns with no missing values, and assign the resulting Series object to full_cols_series
full_cols_series = null_series[null_series==0]

# Determine the correlation of each feature column to the target column
train_subset = train[full_cols_series.index]
corrmat = train_subset.corr()
sorted_corrs = corrmat['SalePrice'].abs().sort_values()

# Limit the check to features with a correlation to the SalePrice >= 0.3
strong_corrs = sorted_corrs[sorted_corrs >= 0.3]
corrmat = train_subset[strong_corrs.index].corr()
fig = plt.subplots()
sns.heatmap(corrmat[strong_corrs.index])

plt.yticks(rotation=0) 
plt.xticks(rotation=90)

plt.show()