# See page 11 from math refresher notebook for more context

# Performing row operations using NumPy
# Instantiate the matrix
# matrix =  np.asarray([[1, 3], [50, 2]], dtype=np.float32)

# Swap the second row (at index value 1) with the first row (at index value 0).
# matrix = matrix[[1,0]]

# Multipy the second row by 2.
# matrix[1] = 2*matrix[1]

# Add the second row to the first row.
# matrix[1] = matrix[1] + matrix[0]

import numpy as np

matrix_one = np.asarray([[30, -1, -500], [50, -1, -100]], dtype=np.float32)

# Divide the first row from matrix_one by 30
matrix_one[0] = (1/30) * matrix_one[0] 
print('matrix_one:', matrix_one)

