n = int(input())
arr = [[0] * n for _ in range(n)]
var_even = n*2-1
var_odd = 1
start = 1

for i in range(n):
    if i != 0:
        start = arr[i-1][0] + 1
        var_even -= 2
        var_odd += 2
    for j in range(n):
        if j != 0:
            if j % 2 == 0:
                start += var_odd
            elif j % 2 != 0:
                start += var_even
        arr[i][j] = start

for i in arr:
    for j in i:
        print(j, end=' ')
    print()