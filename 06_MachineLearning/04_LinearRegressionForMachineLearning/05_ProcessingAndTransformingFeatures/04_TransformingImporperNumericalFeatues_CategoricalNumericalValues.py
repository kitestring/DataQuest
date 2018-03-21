# Create a new column years_until_remod in the train data frame that represents the 
# difference between Year Remod/Add (the later value) and Year Built (the earlier value).

# This code converts nominal/categorical numerical data which contains values that
# don't directly correlate to the target value, into numerical values that do correlate to the target

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460].copy()
test = data[1460:].copy()

train['years_until_remod'] = train['Year Remod/Add'] - train['Year Built']