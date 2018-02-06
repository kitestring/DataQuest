import math
def find_outcome_combinations(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

combinations_7 = find_outcome_combinations(10, 7)
print('combinations_7:', combinations_7)

combinations_8 = find_outcome_combinations(10, 8)
print('combinations_8:', combinations_8)

combinations_9 = find_outcome_combinations(10, 9)
print('combinations_9:', combinations_9)