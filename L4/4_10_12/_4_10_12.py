import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# --- Гілка 1: x < 3 ---
x1_raw = np.linspace(-180, 2.99, 5000)
arg1 = np.cos(np.radians(2 * x1_raw)) / (x1_raw - 0.5)
valid1 = arg1 > 0
x1 = x1_raw[valid1]
y1 = np.log10(arg1[valid1])

# --- Гілка 2: x >= 4 ---
x2_raw = np.linspace(4, 100, 10000)
cos_x2 = np.cos(np.radians(x2_raw))
tan_x2sq = np.tan(np.radians(x2_raw ** 2))
denom2 = 1 + tan_x2sq
arg2 = cos_x2 / denom2
valid2 = (np.abs(denom2) > 1e-6) & (arg2 > 0)
x2 = x2_raw[valid2]
y2 = np.log(arg2[valid2])

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x1, y1, color='steelblue', linewidth=2, label='Гілка 1: x < 3')
ax.plot(x2, y2, color='tomato', linewidth=2, label='Гілка 2: x >= 4')

ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel('x (градуси)', fontsize=13)
ax.set_ylabel('y', fontsize=13)
ax.set_title('Графік функції варіанту 12 (x у градусах)', fontsize=14)
ax.legend(loc='upper right', fontsize=11)
ax.set_ylim(-6, 4)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()