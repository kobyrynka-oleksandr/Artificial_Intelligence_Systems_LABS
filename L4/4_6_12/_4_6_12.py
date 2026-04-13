import numpy as np

variant = 12
K = 7
center = K // 2

matrix = np.zeros((K, K), dtype=int)

for i in range(K):
    for j in range(K):
        if abs(i - center) + abs(j - center) == center:
            matrix[i][j] = variant

print(matrix)