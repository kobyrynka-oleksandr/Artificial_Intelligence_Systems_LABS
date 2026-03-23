def insert_before_index(a, index, value):
    result = []
    
    for i in range(len(a)):
        if i == index:
            result.append(value)
        result.append(a[i])
    
    if index == len(a):
        result.append(value)
    
    return result

n = int(input("Введіть кількість елементів: "))
a = []

for i in range(n):
    a.append(int(input(f"Елемент {i+1}: ")))

index = int(input("Введіть індекс: "))
value = int(input("Введіть число для вставки: "))

result = insert_before_index(a, index, value)

print("Початковий список:", a)
print("Новий список:", result)