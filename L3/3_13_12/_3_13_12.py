def rle_encode(text):
    if not text:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    encoded += text[-1] + str(count)

    return encoded


def rle_decode(encoded):
    decoded = ""
    i = 0

    while i < len(encoded):
        char = encoded[i]
        i += 1

        count_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            count_str += encoded[i]
            i += 1

        decoded += char * int(count_str)

    return decoded


text = input("Введіть рядок: ")

encoded = rle_encode(text)
print("Закодований:", encoded)

decoded = rle_decode(encoded)
print("Декодований:", decoded)