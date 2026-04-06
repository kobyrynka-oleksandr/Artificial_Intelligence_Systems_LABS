def count_substring(s, sub):
    count = 0
    n = len(sub)
    
    for i in range(len(s) - n + 1):
        if s[i:i+n] == sub:
            count += 1
            
    return count


text = input("Введіть рядок: ")
substring = input("Введіть підрядок: ")

result = count_substring(text, substring)

print("Кількість входжень:", result)