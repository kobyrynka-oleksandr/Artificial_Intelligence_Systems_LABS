import random

def generate_list(n, a, b):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(a, b))
    return numbers

n = int(input("Введіть кількість елементів n: "))
a = int(input("Введіть початок інтервалу a: "))
b = int(input("Введіть кінець інтервалу b: "))

if a > b:
    temp = a
    a = b
    b = temp

result = generate_list(n, a, b)

print("Згенерований список:")
print(result)