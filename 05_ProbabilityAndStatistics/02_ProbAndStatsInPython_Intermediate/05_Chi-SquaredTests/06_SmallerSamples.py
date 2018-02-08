from values import chisquared_bimodal

observed_Males = 217.90
observed_Females = 107.71
expected_Males = 162.805
expected_Females = 162.805

gender_chisq = chisquared_bimodal(observedA=observed_Males, expectedA=expected_Males, observedB=observed_Females, expectedB=expected_Females)

print(gender_chisq)