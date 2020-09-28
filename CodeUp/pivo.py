def solution(scoville, K):
    answer = 0

    while True:
        scoville.sort()
        min1 = scoville[0]
        min2 = scoville[1]

        cal = min1 + (min2 * 2)
        answer += 1
        if cal < K:
            scoville.append(cal)
        scoville.remove(min1)
        scoville.remove(min2)

        verify = [x for x in scoville if x < K]
        if len(verify) == 0:
            break
        elif len(verify) == 1:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
