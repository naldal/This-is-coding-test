def solution(phone_number):
    a = ["*" for _ in phone_number[:-4]]
    a += [x for x in phone_number[-4:]]
    return ''.join(a)


print(solution("027778888"))