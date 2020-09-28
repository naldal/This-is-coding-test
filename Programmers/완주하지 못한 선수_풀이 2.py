def solution(participant, completion):
    answer = ''
    dic = {}
    temp = 0
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    print(dic)
    print(temp)

    return answer

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

print(solution(participant, completion))