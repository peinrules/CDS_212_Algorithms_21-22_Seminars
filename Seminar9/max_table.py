# Дано: таблица с числами. 
# Нужно найти путь сверху-слева вправо-вниз, двигаясь вправо или вниз, такой что его сумма будет максимальной.

# Динамика следующая: максимальный путь в заданную точку это будет максимум из путей в две предыдущие

n, m = list(map(int, input().split()))

data = list()
for i in range(n):
    data_i = list(map(int, input().split()))
    data.append(data_i)
dp = [[0 for j in range(m)] for i in range(n)]
dp[0][0] = data[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + data[i][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + data[0][j]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + data[i][j]

print(dp)
print(dp[n - 1][m - 1])
