# Find the probability that 1 coin out of 3 is heads.
from functools import reduce
from operator import mul


single_event_probability = 0.5
three_coin_event = [single_event_probability for _ in range(3)]
combinations = 3
one_toss_event = reduce(mul, three_coin_event, 1)
coin_1_prob = one_toss_event * combinations
print(coin_1_prob)
