import numpy as np

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

dot_product = np.dot(vector_one[:,0], vector_two)
print(dot_product)