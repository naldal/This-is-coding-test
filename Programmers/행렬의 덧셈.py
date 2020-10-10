def solution(arr1, arr2):
    tmp = []
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            a = arr1[i][j]
            b = arr2[i][j]
            tmp.append(a+b)
        answer.append(tmp)
        tmp = []
    return answer



print(solution([[1,2], [2, 3]], [[3,4], [5,6]]))
