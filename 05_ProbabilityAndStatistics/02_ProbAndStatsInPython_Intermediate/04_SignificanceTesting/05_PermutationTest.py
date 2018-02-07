# The lists weight_lost_a and weight_lost_b contain the amount of weight (in pounds)
# that the participants in each group lost.

# Calculate the observed test statistic by subtracting mean_group_a from mean_group_b and assign to mean_difference.

import numpy as np
import matplotlib.pyplot as plt

weight_lost_a = [3, 2, 3, 4, 3, 2, 2, 2, 1, 3, 2, 3, 1, 3, 4, 1, 3, 2, 1, 3, 4, 3, 2, 3, 7, 2, 3, 2, 5, 1, 1, 1, 3, 2, 4, 10, 2, 3, 2, 5, 6, 2, 3, 2, 3, 4, 1, 3, 3, 1]
weight_lost_b = [5, 4, 5, 5, 4, 5, 7, 5, 4, 3, 3, 5, 10, 3, 4, 9, 7, 6, 9, 4, 2, 5, 7, 7, 7, 5, 4, 8, 9, 6, 7, 6, 7, 6, 3, 5, 5, 4, 2, 3, 3, 5, 6, 9, 7, 6, 4, 5, 4, 3]

all_values =  [3, 5, 2, 4, 3, 5, 4, 5, 3, 4, 2, 5, 2, 7, 2, 5, 1, 4, 3, 3, 2, 3, 3, 5, 1, 10, 3, 3, 4, 4, 1, 9, 3, 7, 2, 6, 1, 9, 3, 4, 4, 2, 3, 5, 2, 7, 3, 7, 7, 7, 2, 
               5, 3, 4, 2, 8, 5, 9, 1, 6, 1, 7, 1, 6, 3, 7, 2, 6, 4, 3, 10, 5, 2, 5, 3, 4, 2, 2, 5, 3, 6, 3, 2, 5, 3, 6, 2, 9, 3, 7, 4, 6, 1, 4, 3, 5, 3, 4, 1, 3]

mean_group_a = np.asarray(weight_lost_a).mean()
mean_group_b = np.asarray(weight_lost_b).mean()
mean_difference = mean_group_b - mean_group_a

mean_differences = []

for _ in range(1000):
    group_a = []
    group_b = []
    
    for v in all_values:
        if np.random.rand() >= 0.5:
            group_a.append(v)
        else:
            group_b.append(v)
            
    mean_differences.append(np.asarray(group_b).mean() - np.asarray(group_a).mean())
    
plt.hist(mean_differences)

plt.show()