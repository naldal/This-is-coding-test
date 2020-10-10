from math import sqrt


def solution(n):
    if sqrt(n) != int(sqrt(n)):
        return -1
    else:
        return int(sqrt(n)+1)*int(sqrt(n)+1)


print(solution(121))

