# The lists weight_lost_a and weight_lost_b contain the amount of weight (in pounds)
# that the participants in each group lost. Let's now explore the data to become more familiar with it.

import numpy as np
import matplotlib.pyplot as plt

weight_lost_a = [3, 2, 3, 4, 3, 2, 2, 2, 1, 3, 2, 3, 1, 3, 4, 1, 3, 2, 1, 3, 4, 3, 2, 3, 7, 2, 3, 2, 5, 1, 1, 1, 3, 2, 4, 10, 2, 3, 2, 5, 6, 2, 3, 2, 3, 4, 1, 3, 3, 1]
weight_lost_b = [5, 4, 5, 5, 4, 5, 7, 5, 4, 3, 3, 5, 10, 3, 4, 9, 7, 6, 9, 4, 2, 5, 7, 7, 7, 5, 4, 8, 9, 6, 7, 6, 7, 6, 3, 5, 5, 4, 2, 3, 3, 5, 6, 9, 7, 6, 4, 5, 4, 3]

mean_group_a = np.asarray(weight_lost_a).mean()
mean_group_b = np.asarray(weight_lost_b).mean()

print('mean_group_a:', mean_group_a)
print('mean_group_b:', mean_group_b)

fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
 
ax1.hist(weight_lost_a)
ax1.set_title('weight_lost_a')
ax2.hist(weight_lost_b)
ax2.set_title('weight_lost_b')

plt.show()