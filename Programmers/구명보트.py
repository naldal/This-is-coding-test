def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    boat = 0
    print(people)
    while start <= end:
        total = people[start] + people[end]
        print(total, start, end)
        if total > limit:
            end -= 1
        else:
            start += 1
            end -= 1
        boat += 1

    return boat


print(solution([70, 50, 80, 50], 100))
