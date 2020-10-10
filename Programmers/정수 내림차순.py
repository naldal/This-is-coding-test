def solution(n):
    return int(''.join(list(reversed(sorted([x for x in str(n)])))))

print(solution(118372))