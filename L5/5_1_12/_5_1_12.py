import pandas as pd

K = 7

languages = [
    "Python",
    "C#",
    "Java",
    "JavaScript",
    "C++",
    "Ada",
    "PHP"
]

series = pd.Series(languages[:K], index=range(1, K + 1))

print(series)