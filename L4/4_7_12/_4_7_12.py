import numpy as np

K = 6
N = 12

i, j = np.indices((K, K))
matrix = np.where((i + j) % 2 == 1, N, 0)

print(matrix)