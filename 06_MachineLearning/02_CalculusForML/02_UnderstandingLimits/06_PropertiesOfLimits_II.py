import sympy as s

print('Demonstration of how limits can be broken up with terms that are being multiplied by a constant.\n')

x,y = s.symbols('x y')

y = x**3 + 2*x**2 - 10*x
limit_three = s.limit(y, x, -1)
print('Limit left intact\nlimit_three:', limit_three)

y = (x**3/2) + x**2 - 5*x
limit_three = 2 * s.limit(y, x, -1)
print('\nLimit broken up\nlimit_three:', limit_three)