# На вход дано: строка s
# Найти самую длинную подстроку-палиндром у s.
# Например: cbabd, ответ будет bab

# P[i][j] = True, если s_i...s_j -- палиндром
# P[i][j] = True, если s_i = s_j и строка s_{i+1}...s_{j - 1} -- палиндром

s = input()
n = len(s)
dp = [[False for i in range(n)] for j in range(n)]

for i in range(n):
    dp[i][i] = True

for j in range(n):
    for i in range(n):
        if i >= j:
            continue
        new_i = i + 1
        new_j = j - 1
        if new_i > new_j: # случай, когда мы смотрим на строку из двух элементов.
            if s[i] == s[j]:
                dp[i][j] = True

        else:
            if s[i] == s[j] and dp[new_i][new_j]:
                dp[i][j] = True

# Ответ - длинейшая строка палиндром
max_len = 0
answer = "_"

for i in range(n):
    for j in range(n):
        if dp[i][j] == False:
            continue
        cur_len = j - i + 1
        if cur_len > max_len:
            max_len = cur_len
            answer = s[i:j + 1]
print(answer)
