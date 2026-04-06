def draw_P(n):
    height = 6

    for row in range(height):
        line = ""

        for k in range(1, n + 1):
            num = str(k)

            if row == 0:
                part = " ____ "
            elif row == 1:
                part = "|    \\"
            elif row == 2:
                part = "| " + num.center(3) + "|"
            elif row == 3:
                part = "|____/"
            elif row == 4:
                part = "|     "
            elif row == 5:
                part = "|     "

            line += part + " "

        print(line)


n = int(input("Введіть n (1-9): "))
draw_P(n)