def solution(n, lost, reserve):
    # 초기값 세팅
    students = [1] * n

    for i in lost:
        students[i - 1] -= 1

    for i in reserve:
        students[i - 1] += 1

    print(students)
    for i, v in enumerate(students):
        # value 가 2가 아니면 다음 인덱스로
        if v <= 1 or (i-1 < 0 and students[i+1] != 0):
            continue
        # i-1 이 range 를 넘어가고 다음 인덱스의 값이 0이라면
        if i - 1 < 0 and students[i + 1] == 0:
            students[i + 1] += 1
            students[i] -= 1

        # i+1 이 range 를 넘어가고 이전 인덱스의 값이 0 이라면
        elif i + 1 >= len(students) and students[i - 1] == 0:
            students[i - 1] += 1
            students[i] -= 1

        # 인덱스의 끝에 도달하였는데 이전 인덱스의 값이 0이 아닐 때
        elif i == len(students) - 1 and students[i - 1] != 0:
            continue

        # 단순히 이전 인덱스의 값이 0이라면
        elif students[i - 1] == 0:
            students[i - 1] += 1
            students[i] -= 1

        # 단순히 다음 인덱스의 값이 0이라면
        elif students[i + 1] == 0:
            students[i + 1] += 1
            students[i] -= 1

    answer = [x for x in students if x != 0]

    return len(answer)


# print(solution(5, [2, 4], [1,3,5]))
# print(solution(5, [2, 4], [3]))

# print(solution(4, [1, 3], [4]))
