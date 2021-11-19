# Дано: число N
# На калькуляторе мы можем выполнять три операции: 1) +1 2) *2 3) *3
# Начинаем с 1
# Вопрос: за какое наименьшее число операций можем получить N?

import sys

N = int(input())

if N == 1:
    print(0)
    print(1)
    sys.exit()

prev = list()
min_oper = list()
min_oper.append(0)
# res.append(1)
prev.append(-1)

for i in range(1, N):
    cur_num = i + 1

    pos1 = float("inf") # +1
    pos2 = float("inf") # *2
    pos3 = float("inf") # *3

    pos1 = min_oper[-1]
    if cur_num % 2 == 0:
        pos2 = min_oper[cur_num // 2 - 1]
    if cur_num % 3 == 0:
        pos3 = min_oper[cur_num // 3 - 1]
    
    minimum = min(pos1, pos2, pos3)
    min_oper.append(minimum + 1)
    if minimum == pos1:
        prev.append(i - 1)
    elif minimum == pos2:
        prev.append(cur_num // 2 - 1)
    else:
        prev.append(cur_num // 3 - 1)

print(min_oper[-1])
res = list()
res.append(N)
cur_elem = prev[-1]
while cur_elem != -1:
    res.append(cur_elem + 1)
    cur_elem = prev[cur_elem]

for i in range(len(res) - 1, -1, -1):
    print(res[i], end=" ")
print()
