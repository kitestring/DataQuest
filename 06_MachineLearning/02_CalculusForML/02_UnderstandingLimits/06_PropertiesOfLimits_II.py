import sympy as s

print('Demonstration of how limits can be broken up with terms that are being multiplied by a constant.\n')

X,y = s.symbols('X y')

y = X**3 + 2*X**2 - 10*X
limit_three = s.limit(y, X, -1)
print('Limit left intact\nlimit_three:', limit_three)

y = (X**3/2) + X**2 - 5*X
limit_three = 2 * s.limit(y, X, -1)
print('\nLimit broken up\nlimit_three:', limit_three)