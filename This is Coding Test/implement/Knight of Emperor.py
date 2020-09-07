input_data = input()
# 행
row = int(input_data[1])

# 열
column = int(ord(input_data[0]))-int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps =[(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)