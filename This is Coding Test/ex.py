import sys
from operator import itemgetter

n = int(sys.stdin.readline().rstrip())
array = []

for i in range(n):
    data_tmp = tuple(input().split(' '))
    data = (data_tmp[0], int(data_tmp[1]), data_tmp[2])

    if data[0] == 'I':
        array.append(data)
        if len(array) > 1:
            for j in range(len(array)-1):
                if array[j][1] == data[1] or array[j][2] == data[2]:
                    array.pop()

    elif data[0] == 'D':
        if len(array) > 1:
            for j in range(len(array)-1):
                if array[j][1] == data[1]:
                    array.pop(j)

sorted_array = sorted(array, key=itemgetter(1))
order = list(map(int, input().split()))

for i in order:
    print(sorted_array[i-1][1], sorted_array[i-1][2])




