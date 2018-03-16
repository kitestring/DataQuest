# page 29 in the hand written notes for context

import numpy as np
import matplotlib.pyplot as plt
import sympy

fig = plt.figure()

x,y1,y2 = sympy.symbols('x y1 y2')
x = np.linspace(0, 20, 1000)

y1= -2*x+(5/4)
plt.plot(x,y1,label='y=-2x+5/4')

y2= -2*x+(5/2)
plt.plot(x,y2,label='y=-2x+5/2')

plt.legend()
plt.show()