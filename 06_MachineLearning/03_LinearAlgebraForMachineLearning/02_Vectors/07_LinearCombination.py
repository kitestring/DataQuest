import numpy as np

w = np.asarray([[1],[2]], dtype=np.float32)
v = np.asarray([[3],[1]], dtype=np.float32)

end_point = v*2 - 2*w

print(end_point)