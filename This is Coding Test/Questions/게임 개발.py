n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
x_direction = [-1, 0, 1, 0]
y_direction = [0, 1, 0, -1]
nx, ny = 0, 0
count = 0
while True:
    for i in range(4):
        nx += x + x_direction[i]
        ny += y + y_direction[i]
        print(nx, ny)
        if nx < 0 or nx > n or ny < 0 or ny > m:
            break
        elif board[nx][ny] == 0:
            board[x][y] = 1
            x, y = nx, ny
            count += 1
        elif board[nx][ny] == 1:
            nx, ny = 0, 0
            continue



