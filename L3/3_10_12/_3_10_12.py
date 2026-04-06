def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


text = input("Введіть речення: ")
result = reverse_words(text)
print("Результат:", result)