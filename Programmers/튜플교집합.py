def solution(land):
    answer = 0
    idx = 0

    for idx1, i in enumerate(land):
        print(i)
        for idx2, j in enumerate(i):
            print(j)
            if idx1 == 0:
                answer += max(i)
                idx = i.index(max(i))
            else:
                j[idx] = 0
                answer += max(j)
                idx = j.index(max(i))

    return answer




print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))