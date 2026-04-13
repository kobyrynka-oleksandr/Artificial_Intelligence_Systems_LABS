import numpy as np

K = 5
variant = 12

matrix = np.zeros((K, K), dtype=int)

for i in range(K):
    matrix[i][K - 1 - i] = variant

print(matrix)