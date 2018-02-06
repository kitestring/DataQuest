from scipy.stats import binom

# The sum of all the probabilities to the left of k, including k.
left_16 = binom.cdf(k=16, n=30, p=0.39)

# The sum of all probabilities to the right of k.
right_16 = 1 - left_16

print('left_16:', left_16)
print('right_16:', right_16)