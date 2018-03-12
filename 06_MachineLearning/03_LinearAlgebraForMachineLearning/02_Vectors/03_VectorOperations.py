import matplotlib.pyplot as plt

# This code draws the x and y axis as lines. (Basically makes the grid)
plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-4,4)
plt.ylim(-1,4)

plt.quiver(0, 0, 3, 0, angles='xy', scale_units='xy', scale=1, color='green')
plt.quiver(3, 0, 0, 3, angles='xy', scale_units='xy', scale=1, color='green')

plt.show()