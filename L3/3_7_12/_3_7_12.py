def is_identifier(s):
    if len(s) == 0:
        return False

    if not (s[0].isalpha() or s[0] == "_"):
        return False

    for ch in s:
        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
            return False

    return True


text = input("Введіть слово: ")

if is_identifier(text):
    print("Це правильний ідентифікатор")
else:
    print("Це НЕ ідентифікатор")