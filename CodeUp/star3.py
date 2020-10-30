n = int(input())
for i in range(-n, n + 1):
    x = n - abs(i)
    print(x)
    print(' ' * x + '*' * (x + 1))
