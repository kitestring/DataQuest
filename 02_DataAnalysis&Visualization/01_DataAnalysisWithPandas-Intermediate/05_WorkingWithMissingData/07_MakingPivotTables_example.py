import pandas as pd
import numpy as np

# this basically accomplishes the same things as 06_CalculatingSummaryStatistics.py

titanic_survival = pd.read_csv('titanic_survival.csv')

passenger_class_fares = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=np.mean)

print passenger_class_fares