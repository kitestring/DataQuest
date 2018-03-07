import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=0, stop=3, num=301)

y = -(x**2)+(3*x)-1
fig = plt.figure()
plt.plot(x,y)
plt.show()
