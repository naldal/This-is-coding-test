def findIndex(key):
    global keypad
    key = str(key)
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == key:
                return i, j


def verifyHand(i, j, left, right, hand):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 0

    for move in range(4):
        nx = i + dy[move]  # 상하
        ny = j + dx[move]  # 좌우

        if i == 1 and j == 1:
            print(left, right, nx, ny)

        if nx < 0 or nx > 3 or ny < 0 or ny > 2:
            continue

        for x in range(4):
            nx = i + dy[x]
            ny = j + dx[x]
            if nx == left[0] and ny == left[1]:
                count += 1
            elif nx == right[0] and ny == right[1]:
                count += 1
            if count == 2:
                if hand == "right":
                    return "R"
                else:
                    return "L"

        if nx == left[0] and ny == left[1]:
            return "L"
        elif nx == right[0] and ny == right[1]:
            return "R"
        else:
            l_distance = abs(left[0] - i) + abs(left[1] - j)
            r_distance = abs(right[0] - i) + abs(right[1] - j)

            if (l_distance - r_distance) > 0:
                return "R"
            elif (l_distance - r_distance) < 0:
                return "L"
            else:
                if hand == "right":
                    return "R"
                elif hand == "left":
                    return "L"


def solution(numbers, hand):
    result = []
    right = [3, 2]
    left = [3, 0]
    for num in numbers:
        i, j = findIndex(num)
        # print(result, i, j, num)
        if j == 0:
            result += "L"
            left[0], left[1] = i, j
        elif j == 2:
            result += "R"
            right[0], right[1] = i, j
        elif j == 1:
            d = verifyHand(i, j, left, right, hand)
            result += d
            if d == "L":
                left[0], left[1] = i, j
            elif d == "R":
                right[0], right[1] = i, j

    return ''.join(result)


keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]

print(solution([5, 5, 5, 4, 4, 4, 2, 2, 2, 8, 8, 4], "right"))
