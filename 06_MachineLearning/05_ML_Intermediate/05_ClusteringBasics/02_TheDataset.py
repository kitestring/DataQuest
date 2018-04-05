import pandas as pd

votes = pd.read_csv('114_congress.csv')

print(votes.info())

print('\nPolitical Parties')
print(votes['party'].unique())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 18 columns):
# name     100 non-null object
# party    100 non-null object
# state    100 non-null object
# 00001    100 non-null float64
# 00004    100 non-null float64
# 00005    100 non-null float64
# 00006    100 non-null float64
# 00007    100 non-null float64
# 00008    100 non-null float64
# 00009    100 non-null float64
# 00010    100 non-null float64
# 00020    100 non-null float64
# 00026    100 non-null float64
# 00032    100 non-null float64
# 00038    100 non-null float64
# 00039    100 non-null float64
# 00044    100 non-null float64
# 00047    100 non-null float64
# dtypes: float64(15), object(3)
# memory usage: 14.1+ KB
None

# Political Parties
# ['R' 'D' 'I']