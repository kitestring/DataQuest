print("this mission cannot be run locally as the data used is loaded \"behind the scenes\" and I really don't have access to it")




import matplotlib.pyplot as plt

# This plot is short. It is platykurtic.
# Notice how the values are distributed fairly evenly, and there isn't a large cluster in the middle.
# Student performance varied widely.
plt.hist(test_scores_platy)
plt.ylim(0,3500)
plt.xlim(0,1)
plt.show()

# This plot is tall. It is leptokurtic.
# Most students performed similarly.
plt.hist(test_scores_lepto)
plt.ylim(0,3500)
plt.xlim(0,1)
plt.show()

# The height of this plot neither short nor tall. It is mesokurtic.
plt.hist(test_scores_meso)
plt.ylim(0,3500)
plt.xlim(0,1)
plt.show()

# We can measure kurtosis with the kurtosis function.
# Negative values indicate platykurtic distributions, positive values indicate leptokurtic distributions, and values near 0 are mesokurtic.
from scipy.stats import kurtosis
kurt_platy = kurtosis(test_scores_platy)
kurt_lepto = kurtosis(test_scores_lepto)
kurt_meso = kurtosis(test_scores_meso)

print(kurt_platy)
print(kurt_lepto)
print(kurt_meso)