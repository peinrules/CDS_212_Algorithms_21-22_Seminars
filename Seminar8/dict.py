# Дано: строка s, словарь dict
# Проверить, можно ли представить строку s как конкатенацию слов из dict.
# dp[i] -- можно ли представить s[:i + 1] как ---"---

s = input()

m = int(input())
d = list()
for i in range(m):
    d.append(input())

dp = [False for i in range(len(s))]

for i in range(len(s)):
    for word in d:
        if word == s[i + 1 - len(word):i + 1] and (len(word) == i + 1 or dp[i - len(word)]):
            dp[i] = True
print(dp[len(s) - 1])

