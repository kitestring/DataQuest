from math import factorial
import pandas as pd

def ProbabilityOf_k_OutcomesOutOf_N_Events(N, k, q, p):
    single_combination_probability = (p ** k) * (q ** (N - k))
    possible_outcomes = factorial(N) / (factorial(k) * factorial(N - k))
    return single_combination_probability * possible_outcomes

bikes = pd.read_csv("bike_rental_day.csv")

days_over_5000_riders = bikes[bikes['cnt'] > 5000].shape[0]
total_days = bikes['cnt'].shape[0]
prob_over_5000 = days_over_5000_riders / total_days

p = round(prob_over_5000, 2)
q = 1 - p

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

N = 30

outcome_probs = [ProbabilityOf_k_OutcomesOutOf_N_Events(N, k, q, p) for k in outcome_counts]

print(outcome_probs)