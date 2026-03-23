groups = {
    "КС-23": [25, "Іваненко Іван Іванович"],
    "КН-23": [18, "Петренко Петро Петрович"],
    "КТ-23": [30, "Сидоренко Олена Сергіївна"]
}


def show_menu():
    print("\nМеню:")
    print("1) Кількість студентів у групі")
    print("2) ПІБ старости групи")
    print("3) Кортеж груп (<= заданого значення)")
    print("4) Кортеж груп (>= заданого значення)")
    print("5) Змінити кількість студентів")
    print("6) Змінити ПІБ старости")
    print("7) Додати нову групу")
    print("8) Видалити групу")
    print("9) Множина ПІБ старост вибраних груп")
    print("10) Вихід")


while True:
    show_menu()
    choice = input("Оберіть пункт меню: ")

    if choice == "1":
        group = input("Введіть групу: ")
        if group in groups:
            print("Кількість студентів:", groups[group][0])
        else:
            print("Групу не знайдено!")

    elif choice == "2":
        group = input("Введіть групу: ")
        if group in groups:
            print("Староста:", groups[group][1])
        else:
            print("Групу не знайдено!")

    elif choice == "3":
        limit = input("Введіть максимальну кількість студентів: ")
        if limit.isdigit():
            limit = int(limit)
            result = tuple(g for g in groups if groups[g][0] <= limit)
            print("Результат:", result)
        else:
            print("Некоректний формат!")

    elif choice == "4":
        limit = input("Введіть максимальну кількість студентів: ")
        if limit.isdigit():
            limit = int(limit)
            result = tuple(g for g in groups if groups[g][0] >= limit)
            print("Результат:", result)
        else:
            print("Некоректний формат!")

    elif choice == "5":
        group = input("Введіть групу: ")
        if group in groups:
            new_count = int(input("Нова кількість студентів: "))
            groups[group][0] = new_count
            print("Оновлено!")
        else:
            print("Групу не знайдено!")

    elif choice == "6":
        group = input("Введіть групу: ")
        if group in groups:
            new_head = input("Новий ПІБ старости: ")
            groups[group][1] = new_head
            print("Оновлено!")
        else:
            print("Групу не знайдено!")

    elif choice == "7":
        group = input("Нова група: ")
        if group in groups:
            print("Група вже існує!")
        else:
            count = int(input("Кількість студентів: "))
            head = input("ПІБ старости: ")
            groups[group] = [count, head]
            print("Групу додано!")

    elif choice == "8":
        group = input("Введіть групу для видалення: ")
        if group in groups:
            del groups[group]
            print("Групу видалено!")
        else:
            print("Групу не знайдено!")

    elif choice == "9":
        selected = input("Введіть групи через пробіл: ").split()
        result = []
        seen = set()
        for g in selected:
            if g in groups and groups[g][1] not in seen:
                result.append(groups[g][1])
                seen.add(groups[g][1])
        print("Старости вибраних груп:", result)


    elif choice == "10":
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір!")
