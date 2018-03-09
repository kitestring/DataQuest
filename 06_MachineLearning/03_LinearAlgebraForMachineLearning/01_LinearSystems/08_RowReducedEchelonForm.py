# See page 12-13 from math refresher notebook for more context

import numpy as np

matrix = np.asarray([[30, -1, -1000], [50, -1, -100]], dtype=np.float32)

matrix[0] = matrix[0]/30
print('R1 = R1/30')
print(matrix)

matrix[1] -=  matrix[0]*50
print('\nR2 = R2-(R1*50)')
print(matrix)

matrix[1] =  matrix[1]*(3/2)
print('\nR2 = R2*(3/2)')
print(matrix)

# Unfortunately, rounding issues are making this "off"
# thus I was unable to continue and had to use the values I 
# hand calculated to continue.

matrix_three = np.asarray([
    [1, -1/30, -1000/30],
    [0, 1, 2350]  
], dtype=np.float32)

matrix_three[0] +=  matrix_three[1]*(1/30)
print('\nR1 = R1+(R2*(1/30))')
print(matrix_three)