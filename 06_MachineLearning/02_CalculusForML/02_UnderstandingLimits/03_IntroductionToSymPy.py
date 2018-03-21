import sympy

# Import SymPy and declare X and y as SymPy symbols.
X,y = sympy.symbols('X y')
y = X**2 + 1

print(y)

y = 3*X

print(y)