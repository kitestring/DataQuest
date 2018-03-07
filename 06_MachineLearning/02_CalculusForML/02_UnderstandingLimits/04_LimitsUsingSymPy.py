import sympy

x2,y = sympy.symbols('x2 y')
x2 = 2.9
y = -x2**2+ + 3*x2 - 1

limit_one = sympy.limit((y-(-1))/(x2-3),x2,2.9)

print(limit_one)