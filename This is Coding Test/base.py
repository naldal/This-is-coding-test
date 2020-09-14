n = int(input())
array = []
for _ in range(n-1):
    array.append(int(input()))

array.sort()
flag = False

for x in range(n-2):
    expect = array[x]+1
    if array[x+1] != expect:
        print(expect)
        flag = True
        continue
    elif array[0] != 1:
        print("1")
        break
    elif x == n-3 and flag is False:
        print(array[n-2]+1)


