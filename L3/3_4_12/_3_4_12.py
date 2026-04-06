def is_palindrome(word):
    n = len(word)
    
    for i in range(n // 2):
        if word[i] != word[n - 1 - i]:
            return False
            
    return True


text = input("Введіть слово: ")

if is_palindrome(text):
    print("Це паліндром")
else:
    print("Це не паліндром")