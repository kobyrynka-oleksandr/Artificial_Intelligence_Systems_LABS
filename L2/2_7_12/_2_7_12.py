def in_intervals(x, intervals):
    for interval in intervals:
        left, right = interval
        if left <= x <= right:
            return True
    return False

n = int(input("Кількість елементів списку: "))
numbers = []

for i in range(n):
    numbers.append(float(input(f"Елемент {i+1}: ")))

m = int(input("Кількість проміжків: "))
intervals = []

for i in range(m):
    print(f"Проміжок {i+1}:")
    left = float(input("  Ліва межа: "))
    right = float(input("  Права межа: "))
    intervals.append([left, right])

in_list = []
out_list = []

for x in numbers:
    if in_intervals(x, intervals):
        in_list.append(x)
    else:
        out_list.append(x)

print("Числа, що входять в об'єднання проміжків:", in_list)
print("Числа, що НЕ входять:", out_list)