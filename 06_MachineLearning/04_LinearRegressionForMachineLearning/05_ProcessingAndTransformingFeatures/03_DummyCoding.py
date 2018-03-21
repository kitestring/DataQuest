# Convert all of the text columns in train to the categorical data type.
# Select the Utilities column, return the categorical codes, and display the unique value counts for those codes: train['Utilities'].cat.codes.value_counts()

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460].copy()
test = data[1460:].copy()

train_null_counts = train.isnull().sum()
df_no_mv = train[train_null_counts[train_null_counts==0].index]

text_cols = df_no_mv.select_dtypes(include=['object']).columns
for col in text_cols:
    train[col] = train[col].astype('category')

dummy_cols = pd.DataFrame()
for col in text_cols:
    col_dummies = pd.get_dummies(train[col])
    train = pd.concat([train, col_dummies], axis=1)
    del train[col]
    
print(train.head(5))