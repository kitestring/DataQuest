import sympy as s

print('Demonstration of how limits can be broken up with terms that are being summed.\n')

x,y = s.symbols('x y')

lim_a = s.limit(3*x**2, x, 1)
lim_b = s.limit(3*x, x, 1)
lim_c = s.limit(-3, x, 1)
limit_two = sum([lim_a, lim_b, lim_c])

print('Limit broken up\n\tlimit_two:', limit_two)

y = 3*(x**2) + 3*x - 3
limit_two = s.limit(y, x, 1)

print('\nLimit left intact\n\tlimit_two:', limit_two)