# See page 9 from math refresher notebook for more context

import numpy as np
import matplotlib.pyplot as plt
import sympy

X,y1,y2 = sympy.symbols('X y1 y2')
X = np.linspace(0,50,1000)

y1 = 30*X + 1000
y2 = 50*X + 100

fig = plt.figure()

plt.plot(X,y1,color='orange')
plt.plot(X,y2,color='blue')

plt.show()