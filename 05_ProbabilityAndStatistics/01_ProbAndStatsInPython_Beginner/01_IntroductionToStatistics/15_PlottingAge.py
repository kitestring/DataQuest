import matplotlib.pyplot as plt
import numpy
import pandas 

import pandas
f = "titanic_survival.csv"
titanic_survival = pandas.read_csv(f)
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])

median_age = new_titanic_survival['age'].median()
mean_age = new_titanic_survival['age'].mean()

plt.hist(new_titanic_survival['age'])

plt.axvline(median_age, color="g")
plt.axvline(mean_age, color="r")

plt.show()