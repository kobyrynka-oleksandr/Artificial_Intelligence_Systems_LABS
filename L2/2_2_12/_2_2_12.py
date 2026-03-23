def get_negative_numbers(a):
    negatives = []
    for num in a:
        if num < 0:
            negatives.append(num)
    return negatives

def get_negative_numbers_list_comprehension(a):
    return [num for num in a if num < 0]

n = int(input("Введіть кількість елементів: "))
a = []

for i in range(n):
    a.append(int(input(f"Елемент {i+1}: ")))

result = get_negative_numbers(a)
result_list_comprehension = get_negative_numbers_list_comprehension(a)

print("Початковий список:", a)
print("Від'ємні числа (без використання генератора списку):", result)
print("Від'ємні числа (з використанням генератора списку):", result_list_comprehension)