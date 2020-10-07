import sys
n = int(sys.stdin.readline().rstrip())
data_input = list(map(str, input().split()))
arr = [[0]*n for _ in range(n)]
move = ['R', 'L', 'U', 'D']
x_type = [1, -1, 0, 0]
y_type = [0, 0, -1, 1]
x, y = 0, 0

while data_input:
    order = data_input.pop(0)
    for i in range(4):
        if order == move[i]:
            x += x_type[i]
            y += y_type[i]
            if x < 0 or y < 0:
                x -= x_type[i]
                y -= y_type[i]

    print(y+1, x+1)
