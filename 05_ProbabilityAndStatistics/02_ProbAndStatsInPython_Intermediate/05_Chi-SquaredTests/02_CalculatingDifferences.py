import pandas as pd

income = pd.read_csv('income.csv')

observed_Females = income[income['sex'] == ' Female'].shape[0]
observed_Males = income[income['sex'] == ' Male'].shape[0]

expected_Females = income.shape[0] / 2
expected_Males = income.shape[0] / 2

print('observed_Females:', observed_Females)
print('observed_Males:', observed_Males)

print('expected_Females:', expected_Females)
print('expected_Males:', expected_Males)

female_diff = (observed_Females - expected_Females) / expected_Females
male_diff = (observed_Males - expected_Males) / expected_Males

print('female_diff:', female_diff)
print('male_diff:', male_diff)