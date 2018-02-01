import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)


print('DataQuest.io Example')

# A function that returns the result of a die roll.
def roll():
    return random.randint(1, 6)

random.seed(1)
small_sample = [roll() for _ in range(10)]

# Plot a histogram with 6 bins (1 for each possible outcome of the die roll)
ax1.hist(small_sample, 6)

print('\nMy Practice\n')

random.seed(1)
medium_sample = [roll() for _ in range(100)]
ax2.hist(medium_sample, 6)

random.seed(1)
large_sample = [roll() for _ in range(10000)]
ax3.hist(large_sample, 6)

random.seed(1)
large_sample = [roll() for _ in range(100000)]
ax4.hist(large_sample, 6)

plt.show()