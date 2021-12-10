# Задача -- реализовать класс куча (heap). Структура данных со следующими асимптотиками:
# Добавить элемент -- O(log n), Удалить максимальный элемент -- O(log n), вернуть максимальный элемент -- O(1)
# Что такое куча: в двух словах -- сбалансированное бинарное дерево, такое что каждый элемент не меньше его потомков (если таковые имеются). Сбалансированное -- все уровни дерева (кроме, возможно, последнего) заполнены целиком.
# То есть число элементов в каждой ветке дерева различается не более чем на 1.
# Как храним? Храним в массиве. Корень кучи -- a[0]. И у элемента с индеком i потомками будут элементы с индексами 2i + 1 и 2i + 2.
# Что важно заметить: 1) понятно, что предыдущее предложение целиком задаёт кучу. 2) Если у элемента j нет потомков, то их не будет и у элемента k > j.
# Реализация:
# 1) Максимум -- берём a[0].
# 2) Добавление. Процедура heapify. Добавляем элемент в конец кучи. А далее поднимаем его наверх пока можем. Поднимаем наверх = меняем местами с предком. Во-первых ясно, что структура мин-макс не нарушится. 
# 3) Удаление (максимума). Делаем похожий трюк. Меняем местами корень кучи и последний элемент кучи. Теперь бывший корень уже можно спокойно удалить. Сейчас бывший последний лист находится в корне. Делаем heapify, спускаем этот элемент вниз. Спускать вниз = менять местами с наибольшим потомком. Когда мы в листе (или оба потомка меньше нас), то закончили.

class Heap:
    def __init__(self):
        self.a = list()
    def insert(self, elem):
        self.a.append(elem)
        idx = len(self.a) - 1
        while idx > 0 and self.a[idx] > self.a[(idx - 1) // 2]:
            prev = (idx - 1) // 2
            self.a[idx], self.a[prev] = self.a[prev], self.a[idx]
            idx = prev
    def extract(self):
        print(self.a[0])
        self.a[0], self.a[-1] = self.a[-1], self.a[0]
        self.a.pop()
        idx = 0
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            idx_max = idx
            if left < len(self.a) and self.a[left] > self.a[idx]:
                idx_max = left
            if right < len(self.a) and self.a[right] > self.a[idx_max]:
                idx_max = right
            if idx_max == idx:
                break
            self.a[idx], self.a[idx_max] = self.a[idx_max], self.a[idx]
            idx = idx_max


N = int(input())

heap = Heap()

for i in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0: # Добавление
        heap.insert(cmd[1])
    else:
        heap.extract()

