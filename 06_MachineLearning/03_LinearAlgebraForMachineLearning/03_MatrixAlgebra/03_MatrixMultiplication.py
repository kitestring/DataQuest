# page 22 in the hand written notes for context

import numpy as np

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a, matrix_b)
print('product_ab\n', product_ab)

product_ba = np.dot(matrix_b, matrix_a)
print('\nproduct_ba\n', product_ba)