import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    
    # Uses the provided x values to determine the corresponding y values
    x_0 = x_values[0]
    x_1 = x_values[1]
    y_0 = -1*(x_0**2) + x_0*3 - 1
    y_1 = -1*(x_1**2) + x_1*3 - 1
    
    # Now that we have x & y coordinates we can get slope and intercept
    m = (y_1 - y_0) / (x_1 - x_0)
    b = y_1 - m*x_1
    
    # Using the calculated slope we can get a vector of y values
    # with y = mx+b then plot the sceant line
    y_secant = x*m + b
    plt.plot(x, y_secant, c='green')
    plt.show()
    
draw_secant([3,5])
draw_secant([3,10])
draw_secant([3,15])