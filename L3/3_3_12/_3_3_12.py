def unique_words(sentence):
    words = sentence.split()
    unique = []

    for word in words:
        if word not in unique:
            unique.append(word)

    return unique


text = input("Введіть речення: ")
result = unique_words(text)

print("Список слів без повторень:")
print(result)