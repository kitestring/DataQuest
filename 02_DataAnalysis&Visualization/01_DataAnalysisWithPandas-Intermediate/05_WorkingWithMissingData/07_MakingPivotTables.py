import numpy as np
import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')

passenger_age = titanic_survival.pivot_table(index='pclass', values='age', aggfunc=np.mean)
print(passenger_age)