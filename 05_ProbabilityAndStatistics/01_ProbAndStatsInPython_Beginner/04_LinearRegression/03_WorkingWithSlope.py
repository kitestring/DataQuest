import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
y = 4 * x
plt.plot(x, y)
plt.show()

y = 0.5 * x
plt.plot(x, y)
plt.show()

y = -2 * x
plt.plot(x, y)
plt.show()