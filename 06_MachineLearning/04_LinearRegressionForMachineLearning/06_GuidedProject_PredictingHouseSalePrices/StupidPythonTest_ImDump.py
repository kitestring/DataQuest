import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter='\t')

data = data.drop(['1st Flr SF', 'TotRms AbvGrd', 'SalePrice'], axis =1)

# x = {'a': [1,2,3,4,5,6,7,8],
#      'b': [1,2,3,4,5,6,7,8],
#      'c': [1,2,3,4,5,6,7,8],
#      'd': [1,2,3,4,5,6,7,8],
#      'e': [1,2,3,4,5,6,7,8],
#      'f': [1,2,3,4,5,6,7,8]}
# 
# 
# 
# key_list = list(x.keys())
# print(key_list)
# 
# for key, value in x.items():
#     print('key:', key)
#     print(value)


# values = [22,554,45,45,75,22,8766,3235,1,345,3254,45]
# 
# print(values.index(min(values)))

# existing_cols = data.columns.tolist()
# 
# dropped_colinearity = ['1st Flr SF', 'TotRms AbvGrd', 'Full Bath', 
#                        'Half Bath', 'Garage Cars', 'Bsmt Full Bath', '2nd Flr SF']
# 
# common_elements = list(set(dropped_colinearity).intersection(existing_cols))
# 
# for e in common_elements:
#     print(e)

if not 'SalePrice' in data.columns:
    print('Aww Shit')
else:
    print("It's still here bitch")