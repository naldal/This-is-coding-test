n = int(input())
arr = [0] * 201
arr[0] = 1
arr[1] = 1
i = 2


def recur(n, i):
    if n == 1 or n == 2:
        print(arr[n-1] % 10009)
        return

    arr[i] += arr[i - 1] + arr[i - 2]

    if n == i:
        print(arr[n - 1] % 10009)
        return
    recur(n, i + 1)


recur(n, i)
