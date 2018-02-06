import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy import linspace

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
# recall that scipy.linspace(start, stop, num_elements)
outcome_counts = linspace(0,30,31)

outcome_probs_ten_events = binom.pmf(k=outcome_counts, p=0.39, n=30)
plt.bar(outcome_counts, outcome_probs_ten_events)

plt.show()