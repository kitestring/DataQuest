# page 26 in the hand written notes for context

import numpy as np

A = np.asarray([[30,-1],
                [50,-1]],dtype=np.float32)
c = np.asarray([[-1000],
                [-100]],dtype=np.float32)
A_inverse = np.linalg.inv(A)
solution_x = np.dot(A_inverse,c)

print(solution_x)