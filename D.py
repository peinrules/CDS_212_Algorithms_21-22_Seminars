# Дано: k, число команд. Массив размера k: количество очков, набранной каждой из команд. 
# Нужно вывести турнирную таблицу, соответствующую данном набору очков.

# Давайте попробуем решать жадно. Начнём с последнего игрока. Давайте скажем, что он все свои партии сыграл вничью (имеется ввиду по количеству очков). А остальные проиграл.

k = int(input())
results = list(map(int, input().split()))

pairs = list()
for i in range(k):
    pairs.append([results[i], i])

table = [[0 for i in range(k)] for j in range(k)]

for i in range(k):
    pairs.sort(key = lambda x: x[0])
    for j in range(i + 1, k):
        if pairs[i][0] > 0:
            table[pairs[i][1]][pairs[j][1]] = 1
            table[pairs[j][1]][pairs[i][1]] = 1
            pairs[i][0] -= 1
            pairs[j][0] -= 1
        else:
            table[pairs[i][1]][pairs[j][1]] = 0
            table[pairs[j][1]][pairs[i][1]] = 2
            pairs[i][0] -= 0
            pairs[j][0] -= 2


for i in range(k):
    for j in range(k):
        print(table[i][j], end=' ')
    print()

