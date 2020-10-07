data = input()
count = 0
move_type = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
x = int(data[1])
y = ord(data[0]) - 97

for i in move_type:
    nx = x+i[0]
    ny = y+i[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)

