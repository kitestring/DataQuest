import matplotlib.pyplot as plt
import random
import numpy

def roll():
    return random.randint(1, 6)

def probability_of_one(num_trials, num_rolls):
    """
    This function will take in the number of trials, and the number of rolls per trial.
    Then it will conduct each trial, and record the probability of rolling a one.
    """
    probabilities = []
    for _ in range(num_trials):
        die_rolls = [roll() for _ in range(num_rolls)]
        one_prob = len([d for d in die_rolls if d==1]) / num_rolls
        probabilities.append(one_prob)
    return probabilities

fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

random.seed(1)
small_sample = probability_of_one(300, 50)
ax1.hist(small_sample, bins = 20)
ax1.set_ylim(0,70)
ax1.set_xlim(0,0.4)

random.seed(1)
medium_sample = probability_of_one(300, 100)
ax2.hist(medium_sample, bins=20)
ax2.set_ylim(0,70)
ax2.set_xlim(0,0.4)
 
random.seed(1)
large_sample = probability_of_one(300, 1000)
ax3.hist(large_sample, bins=20)
ax3.set_ylim(0,70)
ax3.set_xlim(0,0.4)

plt.show()

large_sample_std = numpy.std(large_sample)
large_sample_mean = numpy.mean(large_sample)
deviations_from_mean = (0.18 - large_sample_mean) / large_sample_std
over_18_count = len([i for i in large_sample if i >= 0.18])


print(large_sample_mean)
print(large_sample_std)
print(deviations_from_mean)
print(over_18_count)