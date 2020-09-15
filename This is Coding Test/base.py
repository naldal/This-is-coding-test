n = int(input())
sosu = []
flag = False
for i in range(2, n):
    for x in range(1, i+1):
        if i % x == 0 and (x == 1 or x == i):
            flag = True
    if flag is True :
        sosu.append(x)
        flag = False


