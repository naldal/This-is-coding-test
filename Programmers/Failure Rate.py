import collections


def solution(N, stages):
    base = collections.Counter([x+1 for x in range(N+1)])
    print(base)
    counter_ = collections.Counter(stages)
    counter_.subtract(base)
    base = dict(counter_)
    counter_ = dict(sorted(base.items(), key=lambda data: data[0]))
    print(counter_)

    survive = len(stages)
    result = []

    for stage in counter_.items():
        rate = 0
        if stage[0] > N:
            survive -= stage[1] + 1
            continue
        if stage[1] < 0:
            result.append((stage[0], rate))
        else:
            rate = (stage[1]+1) / survive
            result.append((stage[0], rate))
            survive -= stage[1]+1

    result.sort(key=lambda data: data[1], reverse=True)
    # print(result)
    result_ = []
    for i in result:
        result_.append(i[0])

    return result_


# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
