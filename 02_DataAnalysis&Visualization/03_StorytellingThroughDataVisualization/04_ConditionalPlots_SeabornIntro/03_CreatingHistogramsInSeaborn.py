import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
titanic = titanic[cols].dropna()

sns.distplot(titanic["Age"])
plt.show()