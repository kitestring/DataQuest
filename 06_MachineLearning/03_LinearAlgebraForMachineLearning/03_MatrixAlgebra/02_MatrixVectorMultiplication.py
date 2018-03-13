# page 21 in the hand written notes for context

import numpy as np

matrix_a = np.asarray([[0.7,3,9],
                      [1.7,2,9],
                      [0.7,9,2]],
                      dtype=np.float32)
vector_b = np.asarray([[1],
                      [2],
                      [1]],
                      dtype=np.float32)

ab_product = np.dot(matrix_a,vector_b)
print(ab_product)