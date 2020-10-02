def solution(brown, yellow):
    answer = []

    x = (brown-2)//2
    y = 3
    while brown + yellow != x * y:
        y = (brown+yellow)//x
        x, y = x-1, y+1

    answer += x, y
    return answer


print(solution(8, 1))