# page 36 & 37 in the hand written notes for context
# also review the MachineLearning.doc

import numpy as np
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = train[features]
y = train['SalePrice']

xT = np.transpose(X)
xT_x = np.dot(xT,X)
xT_x_inverse = np.linalg.inv(xT_x)
xT_y = np.dot(xT,y)

a = np.dot(xT_x_inverse, xT_y)

print(a)