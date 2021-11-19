# У нас есть лестница. Мы хотим дойти от низа до верха. Можем идти на одну ступеньку вверх, либо перепрыгивать через одну. У каждой ступеньки есть стоимость наступания на неё. Хотим дойти до верха, минимизировав суммарную стоимость.

n = int(input())
costs = list(map(int, input().split()))

optimal_cost = list() # минимальная стоимость подъёма на каждую из ступенек. Мы хотим найти optimal_cost[n - 1]

# optimal_costs[n - 1] = min(optimal_costs[n - 2], optimal_cost[n - 3]) + costs[n - 1]

optimal_cost.append(costs[0])
optimal_cost.append(costs[1]) # если мы шагаем с первой ступеньки, то мы платим за ступание на вторую ступеньку + за ступание на первую (на предыдущем шаге). Иначе платим только за вторую.
for i in range(2, n):
    new_cost = min(optimal_cost[i - 2], optimal_cost[i - 1]) + costs[i]
    optimal_cost.append(new_cost)
print(optimal_cost[n - 1])
