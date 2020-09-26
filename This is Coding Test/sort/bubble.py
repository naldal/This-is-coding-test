n = int(input())
arr = list(map(int, input().split()))
sor = sorted(arr)
count = 0


def bubbleSort(x):
    global count
    length = len(x) - 1
    for i in range(length):
        for j in range(length - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
        count += 1
        if arr == sor:
            return count


print(bubbleSort(arr))
