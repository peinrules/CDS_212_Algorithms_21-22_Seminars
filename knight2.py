# Дано: доска N x M, конь стоит в верхнем левом углу.
# Вопрос, сколько есть маршрутов в правый нижний угол. Конь может ходить:

n, m = list(map(int, input().split()))

dp = [[0 for i in range(m)] for i in range(n)]
dp[0][0] = 1

for diag in range(n + m):
    for i in range(min(diag + 1, n)):
        j = diag - i
        if j >= m:
            continue
        if i + j == 0:
            continue
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        if i - 2 >= 0 and j - 1 >= 0:
            num1 = dp[i - 2][j - 1]
        if i - 1 >= 0 and j - 2 >= 0:
            num2 = dp[i - 1][j - 2]
        if i - 2 >= 0 and j + 1 < m:
            num3 = dp[i - 2][j + 1]
        if i + 1 < n and j - 2 >= 0:
            num4 = dp[i + 1][j - 2]
        dp[i][j] = num1 + num2 + num3 + num4

print(dp[n - 1][m - 1])
