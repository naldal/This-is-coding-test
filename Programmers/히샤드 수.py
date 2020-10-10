def solution(num):
    n = sum([int(x) for x in str(num)])
    return num % n == 0


print(solution(13))