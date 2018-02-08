# Calculated in 02_CalculatingDifferences
observed_Females = 10771
observed_Males = 21790
expected_Females = 16280.5
expected_Males = 16280.5
female_percent_diff = -0.33841098246368356
male__percent_diff = 0.33841098246368356

# Calculated in 03_UpdatingTheFormula
gender_chisq = 3728.950615767329

def chisquared_bimodal(observedA, expectedA, observedB, expectedB):
    diffA = (observedA - expectedA) ** 2 / expectedA
    diffB = (observedB - expectedB) ** 2 / expectedB
    return diffA + diffB