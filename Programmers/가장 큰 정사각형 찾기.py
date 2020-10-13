def solution(board):
    width = len(board[0])
    height = len(board)
    for x in range(1, height):
        for y in range(1, width):
            if board[x][y] == 1:
                board[x][y] = min(board[x-1][y-1], min(board[x-1][y], board[x][y-1])) + 1

    return max([x for element in board for x in element]) ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
