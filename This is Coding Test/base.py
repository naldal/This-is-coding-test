pad = []
for i in range(10):
    pad.append(list(map(int, input().split())))

x, y = 1, 1

while True:
    if pad[x][y] == 2:  # 먹이 발견했을때 break
        pad[x][y] = 9
        break
    elif pad[x + 1][y] == 1 and pad[x][y + 1] == 1:  # 벽으로 가로 막혔을때 break
        pad[x][y] = 9
        break
    pad[x][y] = 9
    if pad[x][y + 1] == 1:  # 오른쪽이 벽이면 아래로 1칸
        x += 1
    elif pad[x + 1][y] == 1:  # 아래쪽이 벽이면 오른쪽으로 1칸
        y += 1
    else:
        y += 1  # 주변에 벽이 없으면 오른쪽으로 1칸
pad[x][y] = 9

for i in pad:
    for j in i:
        print(j, end=' ')
    print()
