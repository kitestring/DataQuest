from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

# Create the cumulative binomial probabilities, one for each entry in outcome_counts.
dist = binom.cdf(k=outcome_counts, n=30, p=0.39)

plt.plot(outcome_counts, dist)
plt.title('Cumulative Density Function\nof 30 events with a probability of 0.39')
plt.show()