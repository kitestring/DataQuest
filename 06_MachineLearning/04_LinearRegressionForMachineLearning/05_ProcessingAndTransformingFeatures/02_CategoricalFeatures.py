# Convert all of the text columns in train to the categorical data type.
# Select the Utilities column, return the categorical codes, and display the unique value counts for those codes: train['Utilities'].cat.codes.value_counts()

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460].copy()
test = data[1460:].copy()

train_null_counts = train.isnull().sum()
df_no_mv = train[train_null_counts[train_null_counts==0].index]

# Selects only the columns that are of type object (string)
text_cols = df_no_mv.select_dtypes(include=['object']).columns
# text_cols = ['MS Zoning', 'Street', 'Lot Shape', 'Land Contour', 'Utilities', 'Lot Config', 'Land Slope', 'Neighborhood', 'Condition 1', 
#              'Condition 2', 'Bldg Type', 'House Style', 'Roof Style', 'Roof Matl', 'Exterior 1st', 'Exterior 2nd', 'Exter Qual', 
#              'Exter Cond', 'Foundation', 'Heating', 'Heating QC', 'Central Air', 'Electrical', 'Kitchen Qual', 'Functional', 'Paved Drive', 'Sale Type', 'Sale Condition']

# Displays the number of unique values for each column that has no missing values & is of type object
# Then converts the column's type to a category
for col in text_cols:
    print(col+":", len(train[col].unique()))
    train[col] = train[col].astype('category')
# Output from loop
#     MS Zoning: 6
#     Street: 2
#     Lot Shape: 4
#     Land Contour: 4
#     Utilities: 3
#     Lot Config: 5
#     Land Slope: 3
#     Neighborhood: 26
#     Condition 1: 9
#     Condition 2: 6
#     Bldg Type: 5
#     House Style: 8
#     Roof Style: 6
#     Roof Matl: 5
#     Exterior 1st: 14
#     Exterior 2nd: 16
#     Exter Qual: 4
#     Exter Cond: 5
#     Foundation: 6
#     Heating: 6
#     Heating QC: 4
#     Central Air: 2
#     Electrical: 4
#     Kitchen Qual: 5
#     Functional: 7

print('\n')
print(train['Utilities'].cat.codes.value_counts())
# Output:
#     0    1457
#     2       2
#     1       1
#     dtype: int64