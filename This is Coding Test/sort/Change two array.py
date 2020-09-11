n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)
sum = 0
for i in range(k):
    a[i] = b[i]

for i in a:
    sum += i
print(a)
print(sum)

