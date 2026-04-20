import pandas as pd
import numpy as np

K = 5

grades = {
    "Проектування та архітектура ПЗ": [85, 90, 78, 92, 88],
    "Паралельні обчислювальні процеси": [76, 84, 91, 70, 95],
    "Unity": [95, 98, 100, 90, 97],
    "СШІ": [88, 72, 85, 91, 79],
    "Комп'ютерна графіка і Web-дизайн": [82, 89, 77, 84, 91],
}

index = [f"Студент {i}" for i in range(1, K + 1)]

df = pd.DataFrame(grades, index=index)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 30)

print("=== Оцінки студентів ===")
print(df)

print("\n=== Середній бал по дисциплінах ===")
print(df.mean().round(2))