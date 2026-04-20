import pandas as pd

df = pd.DataFrame(
    {"Ціна (грн)": [45.50, 12.99, 89.00, 7.20, 150.75, 33.40]},
    index=["Молоко", "Хліб", "М'ясо", "Яйця", "Сир", "Масло"]
)

print("=== Оригінальна таблиця ===")
print(df)

df_sorted = df.sort_values(by="Ціна (грн)", ascending=True)

print("\n=== Відсортовано за ціною (зростання) ===")
print(df_sorted)