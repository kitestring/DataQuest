# pages 24 & 25 in the hand written notes for context

import numpy as np

i_2 = np.identity(2, dtype=np.float32)
i_3 = np.identity(3, dtype=np.float32)

matrix_23 = np.asarray([[5,7, 0],
                         [14,11, 19]],
                         dtype=np.float32)

matrix_33 = np.asarray([[5,7, 9],
                         [14,11, 6],
                         [0,19, 3]],
                         dtype=np.float32)

identity_23 = np.dot(i_2, matrix_23)

identity_33 = np.dot(i_3, matrix_33)

is_identity_23_equal_to_matrix_23 = matrix_23 == identity_23

is_identity_33_equal_to_matrix_33 = matrix_33 == identity_33

print('is_identity_23_equal_to_matrix_23\n', is_identity_23_equal_to_matrix_23)
print('\nis_identity_33_equal_to_matrix_33\n', is_identity_33_equal_to_matrix_33)
