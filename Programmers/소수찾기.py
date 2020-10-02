import itertools


def isPrime(number):
    tmp_n = int(number)
    if tmp_n <= 1:
        return False
    if tmp_n != 1:
        for i in range(2, tmp_n):
            if tmp_n % i == 0:
                return False
        else:
            return True


def solution(numbers):
    answer = 0
    tmp = []
    for i in range(len(numbers)):
        tmp += list(map(''.join, itertools.permutations(numbers, i+1)))

    tmp = set(int(x) for x in tmp)
    print(tmp)
    answers = [x for x in tmp if isPrime(x)]
    answer = len(set(answers))
    return answer


print(solution("17"))