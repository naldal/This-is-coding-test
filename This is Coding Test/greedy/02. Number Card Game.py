n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # data.sort()
    # min_num = data[0]
    min_num = min(data)
    if min_num > result:
        result = min_num

print(result)



