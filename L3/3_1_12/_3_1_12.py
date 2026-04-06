def count_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count


text = input("Введіть рядок: ")
result = count_digits(text)

print("Кількість цифр у рядку:", result)