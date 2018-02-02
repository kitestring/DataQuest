import pandas as pd
import matplotlib.pyplot as plt
import random

income = pd.read_csv('us_income.csv')

def select_random_sample(count):
    random_indices = random.sample(range(0, income.shape[0]), count)
    return income.iloc[random_indices]

random.seed(1)
mean_ratios = []
for i in range(1000):
    sample = select_random_sample(100)
    ratios = sample["median_income_hs"] / sample["median_income_college"]
    mean_ratios.append(ratios.mean())
    
    
plt.hist(pd.Series(mean_ratios).dropna(), bins=20)
plt.title('Raito of median_income_hs to median_income_college')

print("What does the histogram mean...?\n")

explaination = '''The most common ratio of median_income_hs:median_income_college
is ~ 0.64 - 0.65, meaning that high school educated people make roughly
65% of their college educated counter parts in the same county'''
 
print(explaination) 

plt.show()
