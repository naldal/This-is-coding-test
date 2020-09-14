n = int(input())
studentScore = list(map(int, input().split()))
package = []
for i in range(n):
    package.append([studentScore[i], i])

# print(package)
sortResult = sorted(package, key=lambda x: x[0], reverse=True)
# print(sortResult)
result = {}
count = 1
for i in range(n):
    if i != 0:
        if not (sortResult[i - 1][0] == sortResult[i][0]):
            count = i + 1
        result[sortResult[i][1]] = count
    else:
        result[sortResult[i][1]] = 1
for i in range(n):
    print(studentScore[i], result[i])
