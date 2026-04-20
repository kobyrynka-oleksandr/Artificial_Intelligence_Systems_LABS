import pandas as pd

df = pd.read_csv("education.csv")

K = 3
L = 2

print("=== Повний DataFrame ===")
print(df)

print(f"\n=== Перші {K} рядки (.head) ===")
print(df.head(K))

print(f"\n=== Останні {L} рядки (.tail) ===")
print(df.tail(L))