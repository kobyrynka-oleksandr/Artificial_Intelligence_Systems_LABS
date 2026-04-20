import pandas as pd

K = 4
month = "Липень"

index = pd.MultiIndex.from_arrays(
    [
        ["Червень", "Червень", "Липень", "Липень", "Серпень", "Серпень"],
        ["Дніпро", "Десна", "Ірпінь", "Дніпро", "Десна", "Ірпінь"],
    ],
    names=["Місяць", "Водойма"]
)

df = pd.DataFrame(
    {"Кількість риби": [12, 8, 15, 5, 20, 11]},
    index=index
)

print("=== Журнал риболовлі (все літо) ===")
print(df)

print(f"\n=== Перші {K} записи ===")
print(df.head(K))

print("\n=== Статистика вилову за все літо ===")
stats = df["Кількість риби"]
print(f"Середнє:  {stats.mean():.2f} риб")
print(f"Мінімум:  {stats.min()} риб")
print(f"Максимум: {stats.max()} риб")

sum_of_fish = df.loc[month, "Кількість риби"].sum()
print(f"\n=== Сумарний вилов за {month}: {sum_of_fish} риб ===")