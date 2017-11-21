import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

passenger_classes = [1, 2, 3]
fares_by_class = {}
fare = titanic_survival['fare']

for pclass in passenger_classes:
	fares_by_class[pclass] = fare[titanic_survival['pclass'] == pclass].mean()

print(fares_by_class)
