n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
result = 0
while True:
    if k == 0:
        break
    for i in range(k):
        result += first
    k -= 1
    if k == 0:
        break
    result += second

print(result)