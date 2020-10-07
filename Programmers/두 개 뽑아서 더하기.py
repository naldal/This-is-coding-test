# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, //  1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, // 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, // 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
from itertools import cycle


def solution(answers):
    answer = []
    pattern = [
        cycle([1, 2, 3, 4, 5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(pattern[i]) == num:
                scores[i] += 1

    highest = max(scores)
    answer = [i+1 for i, v in enumerate(scores) if v == highest]

    return answer


print(solution([1, 3, 2, 4, 2]))
