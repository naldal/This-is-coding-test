def solution(n):
    sieve = [True] * n*2

    for i in range(2, n+1):
    
        if sieve[i]:
            for j in range(i + i, n+1, i):
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i]]


print(solution(5))
