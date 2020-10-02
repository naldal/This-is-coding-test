import itertools

# def solution(numbers):
#     x = [str(x) for x in numbers]
#     s = ''
#     for i in x:
#         s += i+' '
#
#     s = list(map(str, s.strip().split(' ')))
#     s = list(map(''.join, itertools.permutations(s)))
#     print(max(s))
from operator import itemgetter


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([3, 30, 34, 5, 9]))
