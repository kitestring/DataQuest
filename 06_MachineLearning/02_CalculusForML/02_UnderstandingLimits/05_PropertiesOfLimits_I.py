import sympy as s

print('Demonstration of how limits can be broken up with terms that are being summed.\n')

X,y = s.symbols('X y')

lim_a = s.limit(3*X**2, X, 1)
lim_b = s.limit(3*X, X, 1)
lim_c = s.limit(-3, X, 1)
limit_two = sum([lim_a, lim_b, lim_c])

print('Limit broken up\n\tlimit_two:', limit_two)

y = 3*(X**2) + 3*X - 3
limit_two = s.limit(y, X, 1)

print('\nLimit left intact\n\tlimit_two:', limit_two)