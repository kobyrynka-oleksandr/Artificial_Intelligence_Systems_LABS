def most_frequent_chars(s, char_set):
    counts = {ch: 0 for ch in char_set}

    for c in s:
        if c in counts:
            counts[c] += 1

    max_count = max(counts.values())
    result = [ch for ch in counts if counts[ch] == max_count and max_count > 0]

    return result, max_count


text = input("Введіть рядок: ")
chars = input("Введіть символи (без пробілів): ")

result, freq = most_frequent_chars(text, chars)

if freq == 0:
    print("Жоден із заданих символів не зустрічається")
else:
    print("Найчастіші символи:", result)
    print("Кількість входжень:", freq)