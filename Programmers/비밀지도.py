def makeTwo(decimal, n):
    b = bin(decimal).replace("0b", "")
    tmp = ''
    if len(b) == n:
        return b
    else:
        for i in range(n-len(b)):
            tmp += "0"
        b = tmp + b
        return b


def solution(n, arr1, arr2):
    map1, map2, map3 = [], [], []
    for i in range(n):
        map1.append(makeTwo(arr1[i], n))
        map2.append(makeTwo(arr2[i], n))
    print(map1)
    print(map2)
    tmp = ''
    for i in range(n):
        for j in range(n):
            if map1[i][j] == "1" or map2[i][j] == "1":
                tmp += "1"
            else:
                tmp += "0"
        map3.append(tmp.replace('1', '#').replace('0', ' '))
        tmp = ''
    return map3



n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 =[30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))