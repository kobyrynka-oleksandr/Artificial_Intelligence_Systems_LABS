def remove_number(a, n):
    result = []
    for num in a:
        if num != n:
            result.append(num)
    return result

def remove_number_list_comprehension(a, n):
    return [num for num in a if num != n]


size = int(input("Введіть кількість елементів: "))
a = []

for i in range(size):
    a.append(int(input(f"Елемент {i+1}: ")))

n = int(input("Введіть число, яке потрібно видалити: "))

result = remove_number(a, n)
result_list_comprehension = remove_number_list_comprehension(a, n)

print("Початковий список:", a)
print("Список без числа", n, "(без генератора):", result)
print("Список без числа", n, "(з генератором):", result_list_comprehension)
