# pages 25 & 26 in the hand written notes for context

import numpy as np

# Create a function named matrix_inverse_two() that accepts a 2 x 2 matrix, as a NumPy ndarray, and returns the matrix inverse.This function should first calculate the determinant of the matrix.
    # If the determinant is equal to 0, an error should be returned.
    # If the determinant is not equal to 0, this function should return the matrix inverse.
# Calculate the inverse of matrix_a using the function you just wrote and assign the result to inverse_a.
# Multiply inverse_a with matrix_a and assign the result to i_2. Display i_2 using the print() function.

def matrix_inverse_two(array_22):
    if array_22.shape != (2,2):
        raise Exception('The value provided is not a 2x2 dimensional array.')
    
    a = array_22[0][0]
    b = array_22[0][1]
    c = array_22[1][0]
    d =  array_22[1][1]
    determinant = (a*d) - (b*c)
    
    if determinant == 0:
        raise ValueError('The determinant for this 2x2 array is 0.')
    else:
        inv_det = 1/determinant
        left_mat = np.asarray([[d,-b],
                              [-c,a]])
        return np.dot(inv_det,left_mat)

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
], dtype=np.float32)

inverse_a = matrix_inverse_two(matrix_a)
i_2 = np.dot(inverse_a,matrix_a)
print(i_2)