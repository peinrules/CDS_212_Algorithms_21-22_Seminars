# Из предположения, что мы что-то знаем. А именно, что ответ строится так:
#   есть строка S. И в ответ мы кидаем i * S для самых разных i.
# Допустим ещё проще: строка состоит из повторов одной буквы.
# 15 * 26 * 126
#

def get_hash(string, x):
    result = 0
    for char in string:
        result = (result * x + ord(char)) % 128
    return result

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
for letter in alphabet:
    for length in range(2, 25):
        flag = True
        for x in range(2, 128):
            if get_hash(letter * length, x) != get_hash(letter * length * 2, x):
                flag = False
                break
        if flag == False:
            continue
        else:
            print(letter * length)
"""
N = int(input())
for i in range(1, N + 1):
    print('hhhhhhhhhhhhhhhh' * i)
