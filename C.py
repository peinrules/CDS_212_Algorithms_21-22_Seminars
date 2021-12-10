# Строка S была записана много раз подряд, после чего был взят её префикс и дан нам. Найти минимальную длину исходной строки S. "bcabcab"

# Идея: давайте найдем такое наименьшее i, что z[i] + i = n.
# "bcabcab"
# "...bcab"


def z_foo(s):
    n = len(s)
    z = [0 for i in range(n)]
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            z[i] = 0
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[z[i] + i]:
            z[i] += 1
        if i + z[i] > r and z[i] != 0:
            l, r = i, i + z[i]
    return z

s = input()
z = z_foo(s)

res = len(s)

for i in range(len(s)):
    if z[i] + i == len(s):
        res = i
        break
print(res)
