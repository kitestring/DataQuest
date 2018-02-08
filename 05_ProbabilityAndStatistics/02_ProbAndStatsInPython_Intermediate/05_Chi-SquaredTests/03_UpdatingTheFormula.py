from values import observed_Females, observed_Males, expected_Females, expected_Males

female_diff = (observed_Females - expected_Females) ** 2 / expected_Females

male_diff = (observed_Males - expected_Males) ** 2 / expected_Males

gender_chisq = sum([female_diff, male_diff])

print(gender_chisq)