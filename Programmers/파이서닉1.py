import collections

my_str = input().strip()
col = collections.Counter(my_str)

result = []
for i in col.items():
    if i[1] == max(col.values()):
        result += i[0]

result.sort()
for i in result:
    print(i, end='')

