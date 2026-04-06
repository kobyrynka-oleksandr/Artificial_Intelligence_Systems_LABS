def hide_numbers(number):
    if len(number) != 16 or not number.isdigit():
        return "Помилка: потрібно ввести рівно 16 цифр"

    masked = "**** **** **** " + number[-4:]
    return masked


nums_string = input("Введіть 16-значний номер: ")
result = hide_numbers(nums_string)

print(result)