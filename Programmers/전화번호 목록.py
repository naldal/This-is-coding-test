def solution(phone_book):
    answer = ''
    phone_book.sort()
    dic = {}
    for p1, p2 in zip(phone_book, phone_book[1:]):
        dic[p1] = p2
        if p2.startswith(p1):
            answer = False
            return answer
        else:
            answer = True
    return answer


phone_book = ['12', '123','1235','567','88']
print(solution(phone_book))