import matplotlib.pyplot as plt

# This code draws the x and y axis as lines. (Basically makes the grid)
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(0,10)
plt.ylim(0,5)

plt.quiver(0, 0, 3, 1, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, 6, 2, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(0, 0, 9, 3, angles='xy', scale_units='xy', scale=1, color='orange')

plt.show()