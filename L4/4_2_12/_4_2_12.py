import numpy as np

M = 4
N = 5

matrix = np.full((M, N), 0.5)

for i in range(min(M, N)):
    matrix[i][i] = -1

print("Матриця:")
print(matrix)

corners = [[0, 1], [1, 2]]

r1, c1 = corners[0]
r2, c2 = corners[1]

submatrix = matrix[r1:r2+1, c1:c2+1]

print("\nПідматриця:")
print(submatrix)