import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60, 70])
arr2 = np.array([0, 2, 5])

result = arr1[arr2]

print("Первинний масив:", arr1)
print("Масив індексів:", arr2)
print("Результат:", result)