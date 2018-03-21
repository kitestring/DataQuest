# Generate 3 scatter plots in the same column:
# The first plot should plot the Garage Area column on the X-axis against the SalePrice column on the y-axis.
# The second one should plot the Gr Liv Area column on the X-axis against the SalePrice column on the y-axis.
# The third one should plot the Overall Cond column on the X-axis against the SalePrice column on the y-axis.
# Read more about these 3 columns in the data documentation.

import pandas as pd
import matplotlib.pyplot as plt
# For prettier plots.
import seaborn

# Gr Liv Area (Continuous): Above grade (ground) living area square feet
# Garage Area (Continuous): Size of garage in square feet
# Overall Cond (Ordinal): Rates the overall condition of the house: Rated 10 - 1, 10 being the best

data = pd.read_csv('AmesHousing.txt', delimiter='\t')
train = data.iloc[:1460]
test = data.iloc[1460:]

# Show the Pearson's correlation for each of the training features
print('Garage Area Pearson correlation:', train['Garage Area'].corr(train['SalePrice']))
print('Gr Liv Area Pearson correlation:', train['Gr Liv Area'].corr(train['SalePrice']))
print('Overall Cond Pearson correlation:', train['Overall Cond'].corr(train['SalePrice']))

fig = plt.figure(figsize=(7,15))

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

train.plot(X="Garage Area", y="SalePrice", ax=ax1, kind="scatter")
train.plot(X="Gr Liv Area", y="SalePrice", ax=ax2, kind="scatter")
train.plot(X="Overall Cond", y="SalePrice", ax=ax3, kind="scatter")

plt.show()