# Дано: n, k, s. 
# Требуется заполнить квадрат n x n нулями и единицами так, чтобы в каждом квадрате k x k было ровно s единиц.

# Что есть жадный алгоритм? Мы просто принимаем оптимальное решение на каждом шаге. Оптимальное -- то, которое максимально нас приближает к решению.

# Понятно, что нам надо заполнять квадраты k x k поочереди. Тогда давайте делать это жадно. Сначала заполним первый квадрат k x k, затем второй и т.д.

n, k, s = list(map(int, input().split()))

res = [[0 for i in range(n)] for j in range(n)]

flag = 0
for i in range(k):
    for j in range(k):
        if flag >= s:
            break
        flag += 1
        res[j][i] = 1
    if flag >= s:
        break

# А дальше мы можем просто "зафракталить" наш большой квадрат копиями меньшего. 
# 1 1 0 1 1 0 1
# 1 1 0 1 1 0 1
# 1 0 0 1 0 0 1
# 1 1 0 1 1 0 1
# 1 1 0 1 1 0 1
# 1 0 0 1 0 0 1
# 1 1 0 1 1 0 1

for i in range(n):
    for j in range(n):
        res[i][j] = res[i % k][j % k]


for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()

