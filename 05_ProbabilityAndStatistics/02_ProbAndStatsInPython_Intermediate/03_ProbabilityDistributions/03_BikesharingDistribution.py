# Let's say we're working for the mayor of Washington, DC, Muriel Bowser. 
# She wants to know on how many days out of the next 30 we can expect more than 5000 riders.
# Rather than give her an exact number, which may not be accurate, we can hedge our bets with a 
# probability distribution. This will show her all the possibilities, along with probabilities for each.
# First, we have to find the probability of there being more than 5000 riders in a single day.
# 
# Find the probability of there being more than 5000 riders in a single day (using the cnt column).
# Assign the result to prob_over_5000.

import pandas as pd
bikes = pd.read_csv("bike_rental_day.csv")

days_over_5000_riders = bikes[bikes['cnt'] > 5000].shape[0]
total_days = bikes['cnt'].shape[0]
prob_over_5000 = days_over_5000_riders / total_days
print('prob_over_5000:', prob_over_5000)