import numpy as np
from values import expected_Females, expected_Males, chisquared_bimodal
import matplotlib.pyplot as plt 

gender_chisq_sampling_distribution = [] 

for _ in range(1000):
    random_numbers_vector = np.random.rand(32561,)
    male_frequency = 0
    female_frequency = 0
    for v in random_numbers_vector:
        if v >= 0.5:
            male_frequency += 1
        else:
            female_frequency += 1
            
    gender_chisq_sampling_distribution.append(chisquared_bimodal(observedA=male_frequency, expectedA=expected_Males, observedB=female_frequency, expectedB=expected_Females))

plt.hist(gender_chisq_sampling_distribution)
plt.show()