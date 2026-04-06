def analyze_text(text):
    vowels = "aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZбвгґджзклмнпрстфхцчшщБВГҐДЖЗКЛМНПРСТФХЦЧШЩ"

    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    total_letters = vowel_count + consonant_count

    if total_letters == 0:
        return 0, 0

    vowel_percent = (vowel_count / total_letters) * 100
    consonant_percent = (consonant_count / total_letters) * 100

    return vowel_percent, consonant_percent


text = input("Введіть текст: ")

v_percent, c_percent = analyze_text(text)

print(f"Голосні: {v_percent:.2f}%")
print(f"Приголосні: {c_percent:.2f}%")