n = int(input())
a, b = map(int, input().split())
c = int(input())
tp = []

for i in range(n):
    tp.append(int(input()))

tmp_cal = c
base_price = a
maximum = tmp_cal // base_price
tp = sorted(tp, reverse=True)
for i in range(len(tp)):
    tmp_cal += tp[i]
    base_price += b
    tmp_maximum = tmp_cal // base_price
    # print(tmp_cal, base_price, tmp_maximum, maximum)
    if tmp_maximum > maximum:
        maximum = tmp_maximum

print(maximum)







