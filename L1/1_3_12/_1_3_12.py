import math

def term(x, n, k):
    try:
        numerator = x ** (2*k + 1)
        a = n - k

        base = x + ((-1)**k) * (k + 1)
        power = ((-1)**k) * (k + 1)

        b = base ** power

        denominator = a * b

        if denominator == 0:
            return False, 0

        value = ((-1)**k) * numerator / denominator
        return True, value
    except:
        return False, 0


def calc_for(x, n):
    s = 0
    for k in range(n):
        ok, t = term(x, n, k)
        if not ok:
            return False, 0
        s += t
    return True, s


def calc_while(x, n):
    s = 0
    k = 0
    while k < n:
        ok, t = term(x, n, k)
        if not ok:
            return False, 0
        s += t
        k += 1
    return True, s


def calc_rec(x, n, k=0):
    if k == n:
        return True, 0

    ok, t = term(x, n, k)
    if not ok:
        return False, 0

    ok2, s = calc_rec(x, n, k+1)
    if not ok2:
        return False, 0

    return True, t + s


# main
x = float(input("Введіть x: "))
n = int(input("Введіть n: "))

ok, res = calc_for(x, n)
print("FOR:", res if ok else "Помилка обчислення")

ok, res = calc_while(x, n)
print("WHILE:", res if ok else "Помилка обчислення")

ok, res = calc_rec(x, n)
print("RECURSION:", res if ok else "Помилка обчислення")
