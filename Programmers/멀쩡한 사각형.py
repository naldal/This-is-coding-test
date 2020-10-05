def solution(w, h):
    answer = 1
    block = 0
    if h % w == 0:
        block = w * (w - 1)
    elif w % h == 0:
        block = h * (h - 1)
    else:
        block = w*2
    answer = (w * h) - block
    print(answer)

    return answer


solution(8, 12)
