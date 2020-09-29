import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
flag = True
for number in numbers:
    multiplied *= number
    print(math.sqrt(multiplied))
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')