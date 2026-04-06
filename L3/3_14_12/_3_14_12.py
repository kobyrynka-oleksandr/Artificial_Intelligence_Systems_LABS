import re

def get_words(s: str, delimiters: str) -> list:
    escaped = re.escape(delimiters)
    pattern = f"[{escaped}]+"
    words = re.split(pattern, s)
    return [w for w in words if w]


def is_real_number(word: str) -> bool:
    try:
        float(word)
        return True
    except ValueError:
        return False


def count_real_number_words(s: str, delimiters: str) -> int:
    words = get_words(s, delimiters)
    real_words = [w for w in words if is_real_number(w)]
    return len(real_words), real_words


text = input("Введіть рядок: ")
separators = input("Введіть розділювачі: ")

count, real_words = count_real_number_words(text, separators)

result = count_real_number_words(text, separators)
print(f"\nЗнайдені дійсні числа: {real_words}")
print(f"Кількість слів-дійсних чисел: {count}")