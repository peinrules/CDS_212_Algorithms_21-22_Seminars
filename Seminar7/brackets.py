# Дано: число n. Вывести все правильные скобочные последовательности длины 2n

# ()()((())) ___________ (x) + y

def generate(n):
    dp = [[] for i in range(n + 1)]
    dp[0] = ['']
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
    return dp[-1]

n = int(input())
print(generate(n))

