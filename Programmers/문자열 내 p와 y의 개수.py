def solution(s, n):
    a = [ord(x) for x in s]
    for i, v in enumerate(a):
        if 65 <= v <= 90:
            if v + n > 90:
                v -= 26
            v += n
        elif 97 <= v <= 122:
            if v + n > 122:
                v -= 26
            v += n
        a[i] = chr(v)

    answer = ''
    for i in a:
        answer += i
    return answer

print(solution("Z", 1))
