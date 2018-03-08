# See page 4 from math refresher notebook for hand done math steps
# There we use direct substitution to simplify the equation to y = -2x + 3

import matplotlib.pyplot as plt
import numpy as np
import sympy as s

x = np.linspace(-5,6,110)

c,y = s.symbols('x y')
y = -2 * x + 3

fig = plt.figure()

plt.plot(x,y)
plt.title('This plots the slope of the tangent line at any x value.\nWhich is the derivative of the function.')
plt.xlabel('x value')
plt.ylabel('slope')
plt.show()