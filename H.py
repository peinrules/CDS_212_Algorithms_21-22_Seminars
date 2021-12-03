# Отличие задачи в том, что нам нужно вывести не только лишь наибольшую стоимость, а и посчитать, какие предметы в эту стоимость входят.

N, M = list(map(int, input().split()))
vols = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [-1 for i in range(M + 1)]
dp[0] = 0
dp_ans = [list() for i in range(M + 1)]

for i in range(N):
    for j in range(M - vols[i], -1, -1):
        if dp[j] == -1:
            continue
        else:
            if dp[j + vols[i]] < dp[j] + costs[i]:
                dp[j + vols[i]] = dp[j] + costs[i]
                dp_ans[j + vols[i]] = dp_ans[j][:]
                dp_ans[j + vols[i]].append(i + 1)

maximum = max(dp)
pos = dp.index(maximum)
for i in range(len(dp_ans[pos])):
    print(dp_ans[pos][i])

