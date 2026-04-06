def find_treasure():
    x = 0
    y = 0

    while True:
        line = input()

        if line == "Treasure!":
            break

        direction, steps = line.split()
        steps = int(steps)

        if direction == "East":
            x += steps
        elif direction == "West":
            x -= steps
        elif direction == "North":
            y += steps
        elif direction == "South":
            y -= steps

    print(x, y)

find_treasure()