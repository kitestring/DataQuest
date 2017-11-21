import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
titanic = titanic[cols].dropna()

sns.set_style("white")


g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
plt.xlabel("Age")
sns.despine(left=True, bottom=True)

plt.show()
