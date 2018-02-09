from scipy.stats import chisquare
import numpy as np

expected_males_over50k = 5249.8
expected_males_under50k = 16533.5
expected_females_over50k = 2597.4
expected_females_under50k = 8180.3

observed_males_over50k = 6662
observed_males_under50k = 15128
observed_females_over50k = 1179
observed_females_under50k = 9592

expected = np.array([expected_males_over50k, expected_males_under50k, expected_females_over50k, expected_females_under50k])
observed = np.array([observed_males_over50k, observed_males_under50k, observed_females_over50k, observed_females_under50k])

chisq_gender_income, pvalue_gender_income = chisquare(observed, expected)

print('chisq_gender_income:', chisq_gender_income)
print('pvalue_gender_income:', pvalue_gender_income)