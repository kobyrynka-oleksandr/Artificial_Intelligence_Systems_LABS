import pandas as pd

df = pd.read_csv("education.csv")

print("=== Вміст файлу education.csv ===")
print(df)

print(f"\nРозмір DataFrame: {df.shape}")
print(f"Кількість рядків:  {df.shape[0]}")
print(f"Кількість стовпців: {df.shape[1]}")