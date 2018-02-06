# Find the probability of a single combination for finding 3 days out of 5 are sunny.
# The combination is Sunny, Sunny, Sunny, Not Sunny, Not Sunny.
# Given the following:
    # p is the probability of a sunny day which is 0.7
    # q is the probability of a Not sunny day which is 0.3
    
p = 0.7
q = 0.3

prob_combination_3 = (p**3) * (q**2)
print(prob_combination_3)