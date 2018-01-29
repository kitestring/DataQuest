import matplotlib.pyplot as plt
# import numpy
import pandas 
from scipy.stats import skew
from scipy.stats import kurtosis

import pandas
f = "titanic_survival.csv"
titanic_survival = pandas.read_csv(f)
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])

median_age = new_titanic_survival['age'].median()
mean_age = new_titanic_survival['age'].mean()
skew_age = skew(new_titanic_survival['age'])
kurtosis_age_FTrue = kurtosis(new_titanic_survival['age'], fisher=True)
kurtosis_age_FFalse = kurtosis(new_titanic_survival['age'], fisher=False)

print('median_age =', median_age)
print('mean_age =', mean_age)
print('skew_age =', skew_age)
print('kurtosis_age_FTrue =', kurtosis_age_FTrue)
print('kurtosis_age_FFalse =', kurtosis_age_FFalse)

print("\nOk, let me do my best to summarize this dataset.")

dataSummary = """
The median_age, mean_age, and histogram show that that the majority 
of the people on the ship are between 20-40 years old. Due to that fact it would be expected
to see more people under the age of 20, beasue the most common age of parents is the 20-40
majority.  The skew_age shows us that there are more age groups of people above the mean/median than below it.
The kurtosis show us that his dataset isn't far off from being a normal distribution."""

print(dataSummary)

plt.hist(new_titanic_survival['age'])
 
plt.axvline(median_age, color="g")
plt.axvline(mean_age, color="r")
 
plt.show()