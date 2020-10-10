from math import gcd


def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n
    answer.append(gcd(n, m))
    lc = (n * m) // gcd(n, m)
    answer.append(lc)

    return answer


print(solution(5, 10))
