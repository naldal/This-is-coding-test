n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(m)]
print(board)


def solution(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        solution(x + 1, y)
        solution(x, y + 1)
        solution(x - 1, y)
        solution(x, y - 1)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if solution(i, j):
            count += 1

print(count)
