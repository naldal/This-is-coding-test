def solution(a, b):
    if a > b:
        a, b = b, a
    result = 0
    while a <= b:
        result += a
        a += 1

    return result



