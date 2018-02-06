import math

def ProbOfSingleCombination(k,N,p,q):
    return (p ** k) * (q ** (N-k))

def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

prob_8 = ProbOfSingleCombination(k=8, N=10, p=0.6, q=0.4) * find_outcome_combinations(k=8, N=10)
prob_9 = ProbOfSingleCombination(k=9, N=10, p=0.6, q=0.4) * find_outcome_combinations(k=9, N=10)
prob_10 = ProbOfSingleCombination(k=10, N=10, p=0.6, q=0.4) * find_outcome_combinations(k=10, N=10)

print("prob_8:", prob_8)
print("prob_9:", prob_9)
print("prob_10:", prob_10)