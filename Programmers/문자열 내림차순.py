def solution(s):
    low = [x for x in s if x.islower()]
    up = [x for x in s if x.isupper()]
    result = sorted(low, reverse=True)+sorted(up, reverse=True)
    return ''.join(result)


print(solution("Zbcdefg"))
