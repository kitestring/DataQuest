import numpy as np
import matplotlib.pyplot as plt
import sympy

x,y1,y2 = sympy.symbols('x y1 y2')
x = np.linspace(0,50,1000)

y1 = 30*x + 1000
y2 = 50*x + 100

fig = plt.figure()

plt.plot(x,y1,color='orange')
plt.plot(x,y2,color='blue')

plt.show()