import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

print(solution(participant, completion))


p = collections.Counter(participant)
c = collections.Counter(completion)
print(p - c)
print(list((p-c).keys())[0])