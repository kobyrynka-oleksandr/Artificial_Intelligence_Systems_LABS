while True:
    n = input("n: ")

    if n.isdigit():
        n = int(n)
        break

    print("НЕВІРНИЙ ФОРМАТ! Введіть int-ове число, яке >=1")

possible = set(range(1, n + 1))

while True:
    line = input().strip()
    
    if line == "Все":
        break
    
    try:
        numbers = list(map(int, line.split()))
        if not numbers:
            raise ValueError("немає чисел")
        if any(x < 1 or x > n for x in numbers):
            raise ValueError("числа поза 1..n")
    except ValueError:
        print("НЕВІРНИЙ ФОРМАТ! Введіть 'Все' або числа через пробіл (1..n)")
        continue

    question = set(map(int, line.split()))
    
    yes_set = possible & question
    no_set = possible - question
    
    if len(yes_set) > len(no_set):
        print("Так")
        possible = yes_set
    else:
        print("Ні")
        possible = no_set

result = sorted(possible)
print(*result)