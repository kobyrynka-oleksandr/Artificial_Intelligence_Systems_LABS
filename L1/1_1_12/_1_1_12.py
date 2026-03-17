import math

try:
    x = float(input("Введіть x (у градусах): "))

    if x < 3:
        print("Використовується функція: lg(cos(2x)/(x-0.5))")

        denominator = x - 0.5
        if denominator == 0:
            print("Помилка: знаменник (x - 0.5) дорівнює нулю.")
        else:
            cos_value = math.cos(math.radians(2 * x))
            value = cos_value / denominator

            if value <= 0:
                print("Помилка: аргумент логарифма ≤ 0.")
            else:
                y = math.log10(value)
                print("y =", y)

    elif x >= 4:
        print("Використовується функція: ln(cos(x)/(1+tg(x^2)))")

        cosx = math.cos(math.radians(x))
        tanx2 = math.tan(math.radians(x ** 2))

        denominator = 1 + tanx2
        if denominator == 0:
            print("Помилка: знаменник (1 + tg(x²)) дорівнює нулю.")
        else:
            value = cosx / denominator

            if value <= 0:
                print("Помилка: аргумент ln ≤ 0.")
            else:
                y = math.log(value)
                print("y =", y)

    else:
        print("Функція не визначена при 3 ≤ x < 4.")

except ValueError:
    print("Помилка: введено не число.")