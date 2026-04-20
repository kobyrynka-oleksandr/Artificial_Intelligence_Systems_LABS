import pandas as pd

prices = pd.Series(
    [45.50, 12.99, 89.00, 7.20, 150.75, 33.40],
    index=["Молоко", "Хліб", "М'ясо", "Яйця", "Сир", "Масло"]
)

print("=== Series із цінами на товари ===")
print(prices)

print("\n--- За текстовою міткою (.loc) ---")
label = "М'ясо"
print(f"Ціна на 'М'ясо':  {prices.loc[label]} грн")
print(f"Ціна на 'Молоко': {prices.loc['Молоко']} грн")

print("\n--- За числовим індексом (.iloc) ---")
print(f"Елемент з індексом 0: {prices.iloc[0]} грн")
print(f"Елемент з індексом 2: {prices.iloc[2]} грн")