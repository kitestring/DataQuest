# Read AmesHousing.txt into a dataframe using the tab delimiter (\t) and assign to data.
# Select the first 1460 rows from from data and assign to train.
# Select the remaining rows from data and assign to test.
# Use the dataframe.info() method to display information about each column.
# Read the data documentation to get more familiar with each column.
# Using the data documentation, determine which column is the target column we want to predict. Assign the column name as a string to target.

# I'm thinking to start ALL continuous training features should be used.  
# Each ordinal feature should be considered
# Some of the nominal features are highly important as well
    # example Sale Condition is going to carry a large amount of weight as to the selling price: Normal vs foreclosure or short sale
    
# Per usual, I believe I'm digging in much deeper than the scope of this lesson

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

print(data.info())

target = 'SalePrice'

continuous = ['Lot Frontage', 'Lot Area', 'Mas Vnr Area', 'BsmtFin SF 1', 'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
              '1st Flr SF', '2nd Flr SF', 'Low Qual Fin SF', 'Gr Liv Area', 'Garage Area', 'Wood Deck SF', 'Open Porch SF',
              'Enclosed Porch', '3-Ssn Porch', 'Screen Porch', 'Pool Area', 'Misc Val']