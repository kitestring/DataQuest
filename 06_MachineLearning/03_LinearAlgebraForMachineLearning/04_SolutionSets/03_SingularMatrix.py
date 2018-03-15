# page 30 in the hand written notes for context

import numpy as np

A = np.asarray([[8,4],
                [4,2]], dtype=np.float32)

det = np.linalg.det(A)

print(det)