import numpy as np

M = 4
N = 5

matrix = np.full((M, N), 0.5)

for i in range(min(M, N)):
    matrix[i][i] = -1

print(matrix)