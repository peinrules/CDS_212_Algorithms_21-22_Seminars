# N -- высота здания
# A, B, C -- числа.

# На самом деле -- примерно та же задача о рюкзаке, но каждого из предметов (веса -- А, Б, С) у нас неограниченное количество.

N = int(input())
data = list(map(int, input().split()))

dp = [0 for i in range(N)]
dp[0] = 1

for i in range(len(data)):
    # дальше решение абсолютно такое же, с учётом того, что на пофиг на переиспользование предметов.
    for j in range(data[i], N):
        if dp[j - data[i]] == 0:
            continue
        else:
            dp[j] = 1

res = 0
for i in range(len(dp)):
    if dp[i] == 1:
        res += 1
print(res)
