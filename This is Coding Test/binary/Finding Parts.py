import sys

n = int(sys.stdin.readline().rstrip())
array1 = list(map(int, input().split()))
array1.sort()
m = int(sys.stdin.readline().rstrip())
array2 = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in array2:
    result = binary_search(array1, i, 0, n - 1)
    if result is None:
        print("no")
    else:
        print("yes")
