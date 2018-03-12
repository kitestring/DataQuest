import numpy as np

vector_one = np.asarray([[1],[2],[1]], dtype=np.float32)
vector_two = np.asarray([[3],[0],[1]], dtype=np.float32)
vector_linear_combination = 5 * vector_two + 2 * vector_one

print(vector_linear_combination)