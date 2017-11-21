import pandas as pd
import numpy as np

titanic_survival = pd.read_csv('titanic_survival.csv')

vals = ['fare','survived']

port_stats = titanic_survival.pivot_table(index='embarked', values=vals, aggfunc=np.sum)

print(port_stats)