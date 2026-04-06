import re

def censor_text(text, banned_words):
    pattern = r'\b(' + '|'.join(map(re.escape, banned_words)) + r')\b'
    
    censored = re.sub(pattern, "[ЦЕНЗУРА]", text, flags=re.IGNORECASE)
    
    return censored


text = input("Введіть текст: ")
banned = input("Введіть заборонені слова через кому: ").split(',')

banned = [word.strip() for word in banned]

result = censor_text(text, banned)
print("Результат:", result)