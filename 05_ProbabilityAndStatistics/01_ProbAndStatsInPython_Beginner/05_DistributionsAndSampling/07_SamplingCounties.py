import pandas as pd
import matplotlib.pyplot as plt

income = pd.read_csv('us_income.csv')


# This is the mean median income in any US county.
mean_median_income = income["median_income"].mean()
print(mean_median_income)

def get_sample_mean(start, end):
    return income["median_income"][start:end].mean()

def find_mean_incomes(row_step):
    mean_median_sample_incomes = []
    # Iterate over the indices of the income rows
    # Starting at 0, and counting in blocks of row_step (0, row_step, row_step * 2, etc).
    for i in range(0, income.shape[0], row_step):
        # Find the mean median for the row_step counties from i to i+row_step.
        mean_median_sample_incomes.append(get_sample_mean(i, i+row_step))
    return mean_median_sample_incomes

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

nonrandom_sample = find_mean_incomes(100)
ax1.hist(nonrandom_sample, 20)
ax1.set_title('Bias Sampling')

# What you're seeing above is the result of biased sampling.
# Instead of selecting randomly, we selected counties that were next to each other in the data.
# This picked counties in the same state more often that not, and created means that didn't represent the whole country.
# This is the danger of not using random sampling -- you end up with samples that don't reflect the entire population.
# This gives you a distribution that isn't normal.

import random
def select_random_sample(count):
    random_indices = random.sample(range(0, income.shape[0]), count)
    return income.iloc[random_indices]

random.seed(1)

# Ok, i get this now... I think
# Each iteration of: select_random_sample(100)["median_income"].mean()
# will give me 100 randomly selected median_income values
# Every time through the 100 is different and this is done 1000 times
# Thus your list is 1000 median_income means generated from 100 randomly selected counties

random_sample = [select_random_sample(100)["median_income"].mean() for _ in range(1000)]

for i in random_sample:
    print(i)

ax2.hist(random_sample, 20)
ax2.set_title('Random Sampling')
plt.show()