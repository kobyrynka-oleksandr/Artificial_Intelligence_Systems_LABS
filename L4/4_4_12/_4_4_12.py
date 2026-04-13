import numpy as np

arr = np.array([3, 15, 7, 42, 1, 28, 9, 50, 6, 33])
threshold = 10

greater = arr[arr > threshold]

lesser = arr[arr < threshold]

print("Початковий масив:", arr)
print(f"Більші за {threshold}:", greater)
print(f"Менші за {threshold}:", lesser)
