import numpy as np
import matplotlib.pyplot as plt

K = 15
L = 5
N = 12

arr = np.random.randint(L, N + 1, K).astype(float)

arr_norm = (arr - arr.min()) / (arr.max() - arr.min())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(range(K), arr)
ax1.set_title("Початковий масив")
ax1.set_xlabel("Індекс")
ax1.set_ylabel("Значення")

ax2.bar(range(K), arr_norm, color='orange')
ax2.set_title("Нормалізований масив")
ax2.set_xlabel("Індекс")
ax2.set_ylabel("Значення [0, 1]")

plt.tight_layout()
plt.show()