input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
result = 0
for step in steps:
    n_row = row + step[0]
    n_col = column + step[1]

    if 1 <= n_row <= 8 and 1 <= n_col <= 8:
        result += 1

print(result)
