# Нам дан массив чисел. Требуется расставить их в таком порядке, дабы получившееся число оказалось как можно больше.
# Пример: [3, 30, 34, 5, 9].  Ответ: 9534330

class lex_comp(str):
    def __lt__(x, y):
        # было предложено: если x > y в лексикографическом порядке, то return True
        return x + y > y + x

data = list(input().split())

res = ''.join(sorted(data, key=lex_comp))
if res[0] == '0':
    print(0)
else:
    print(res)

