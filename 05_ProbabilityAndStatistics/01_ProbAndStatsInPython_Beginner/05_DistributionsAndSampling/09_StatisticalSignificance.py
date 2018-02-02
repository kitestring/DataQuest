import pandas as pd
import random

income = pd.read_csv('us_income.csv')

significance_value = None

def select_random_sample(count):
    random_indices = random.sample(range(0, income.shape[0]), count)
    return income.iloc[random_indices]

random.seed(1)
mean_ratios = []
for i in range(1000):
    sample = select_random_sample(100)
    ratios = sample["median_income_hs"] / sample["median_income_college"]
    mean_ratios.append(ratios.mean())
    
mean_ratios_above_five_year_mean = len([i for i in mean_ratios if i >= 0.675])

significance_value = mean_ratios_above_five_year_mean / len(mean_ratios)
print(significance_value)