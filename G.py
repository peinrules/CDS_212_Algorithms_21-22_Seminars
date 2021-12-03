# Максимальная стоимость
# Дано N -- число предметов, M -- вместимость
# a_1, ..., a_N - веса
# b_1, ..., b_N - стоимости
# Задача -- положить в рюкзак предметы с максимальной общей стоимостью.

N, M = list(map(int, input().split()))
vols = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [-1 for i in range(M + 1)] # но теперь это не "можно ли набить рюкзак на вес i", а максимальная стоимость рюкзака при набитии его на вес i.
dp[0] = 0

for i in range(N):
    # давайте докинем i-ый предмет и посмотрим на новую оптимальную стоимость.
    for j in range(M - vols[i], -1, -1):
        # есть dp[j]. если это -1, то фигня. 
        if dp[j] == -1:
            continue
        else:
            dp[j + vols[i]] = max(dp[j + vols[i]], dp[j] + costs[i])
print(max(dp))
