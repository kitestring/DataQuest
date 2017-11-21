import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
titanic = titanic[cols].dropna()

sns.set_style("white")


# The seaborn.FacetGrid object is used to represent the layout of the plots in the grid and the columns used for subsetting the data
# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(titanic, col="Pclass", size=6) # Setting the size parameter to 6 specifies a height of 6 inches for each plot

# the FacetGrid.map() method to specify the plot we want for each unique value of Survived
# For each subset of values, generate a kernel density plot of the "Age" columns.
g.map(sns.kdeplot, "Age", shade=True)

# The function that's passed into FacetGrid.map() has to be a valid matplotlib or seaborn function

plt.xlabel("Age")
sns.despine(left=True, bottom=True)


plt.show()

# Seaborn handled:
# 
# subsetting the data into rows where Survived is 0 and where Survived is 1
# creating both Axes objects, ensuring the same axis scales
# plotting both kernel density plots