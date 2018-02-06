import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy import linspace

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

# Create a range of numbers from 0 to 10, with 11 elements (each number has one entry).
# recall that scipy.linspace(start, stop, num_elements)
outcome_counts = linspace(0,10,11)

outcome_probs_ten_events = binom.pmf(k=outcome_counts, p=0.39, n=10)
ax1.bar(outcome_counts, outcome_probs_ten_events)
ax1.set_title('10 Events')

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
# recall that scipy.linspace(start, stop, num_elements)
outcome_counts = linspace(0,100,101)
outcome_probs_hundred_events = binom.pmf(k=outcome_counts, p=0.39, n=100)
ax2.bar(outcome_counts, outcome_probs_hundred_events)
ax2.set_title('100 Events')

# Create a range of numbers from 0 to 1000, with 1001 elements (each number has one entry).
# recall that scipy.linspace(start, stop, num_elements)
outcome_counts = linspace(0,1000,1001)
outcome_probs_lots_events = binom.pmf(k=outcome_counts, p=0.39, n=1000)
ax3.bar(outcome_counts, outcome_probs_lots_events)
ax3.set_title('1000 Events')

plt.show()