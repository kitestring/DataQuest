import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

correct_mean_fare = titanic_survival['fare'].mean()

print(correct_mean_fare)