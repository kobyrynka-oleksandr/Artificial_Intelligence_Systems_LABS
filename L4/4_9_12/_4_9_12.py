import numpy as np
import matplotlib.pyplot as plt

K, L = 10, 12
np.random.seed(7)
image = np.random.randint(0, 256, (K, L)).astype(float)

smoothed = image.copy()
smoothed[1:-1, 1:-1] = (
    image[0:-2, 0:-2] + image[0:-2, 1:-1] + image[0:-2, 2:] +
    image[1:-1, 0:-2] + image[1:-1, 1:-1] + image[1:-1, 2:] +
    image[2:,   0:-2] + image[2:,   1:-1] + image[2:,   2:]
) / 9

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
ax1.set_title('Оригінал (шум)')
ax1.set_xlabel('Стовпець')
ax1.set_ylabel('Рядок')

im = ax2.imshow(smoothed, cmap='gray', vmin=0, vmax=255)
ax2.set_title('Після згладжування')
ax2.set_xlabel('Стовпець')
plt.colorbar(im, ax=ax2, label='Яскравість (0–255)')

plt.suptitle('Згладжування: середнє арифметичне 8 сусідів')
plt.tight_layout()
plt.show()