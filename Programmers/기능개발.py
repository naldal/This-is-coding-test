def solution(progress, speeds):
    answer = []
    count = 1
    left = [100 - x for x in progress]
    day_deploy = []
    for i in range(len(left)):
        day_deploy.append(left[i] // speeds[i])

    point = day_deploy[0]
    leni = len(day_deploy) - 1
    print(day_deploy)
    for x in range(1, len(day_deploy)):
        if point >= day_deploy[x]:
            count += 1
        else:
            answer.append(count)
            count = 1
            point = day_deploy[x]

        if x == leni:
            answer.append(count)

    return answer


progress = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progress, speeds))
