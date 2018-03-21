import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(start=0, stop=3, num=301)

y = -(X**2)+(3*X)-1
fig = plt.figure()
plt.plot(X,y)
plt.show()
