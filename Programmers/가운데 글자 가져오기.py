def solution(s):
    answer = ''
    point = len(s)//2

    if len(s) % 2 != 0:
        answer = s[point]
    else:
        answer = s[point-1]+s[point]
    return answer

print(solution("abcde"))