def solution(n):
    answer = ''
    a = ['4', '1', '2']

    while n:
        n, mod = divmod(n, 3)
        print(n, mod)
        answer = a[mod] + answer

        if mod == 0:
            n -= 1
    print(answer)
    return answer

solution(4)
