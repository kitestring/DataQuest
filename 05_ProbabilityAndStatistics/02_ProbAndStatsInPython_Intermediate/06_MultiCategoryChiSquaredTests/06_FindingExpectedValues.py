import pandas as pd
from scipy.stats import chi2_contingency

income = pd.read_csv('income.csv')

observed_values = pd.crosstab(income["sex"], [income["race"]])

chisq_value, pvalue_gender_race, degreesoffreedom, expected = chi2_contingency(observed_values)

print('chisq_value:', chisq_value)
print('pvalue_gender_race:', pvalue_gender_race)
print('degreesoffreedom:', degreesoffreedom)
print('\nexpected\n', expected)