# Дано: массив чисел. Нужно проверить, можем ли мы допрыгать от начала до конца.
# Пример: [2, 3, 1, 1, 4]. [3, 2, 1, 0, 4]

nums = list(map(int, input().split()))
n = len(nums)
goal = n - 1
for i in range(n - 1, -1, -1):
    # Если мы из индекса i можем попасть в goal, то давайте i будет новый goal.
    if i + nums[i] >= goal:
        goal = i
if goal == 0:
    print('Yes')
else:
    print('No')
