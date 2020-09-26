from operator import itemgetter

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    arr[i].append(i+1)

sorted_arr = sorted(arr, reverse=True, key=itemgetter(0, 1))

for i in sorted_arr:
    print(i[2], i[0], i[1])