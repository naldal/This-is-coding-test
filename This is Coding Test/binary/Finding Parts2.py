import sys
n = int(sys.stdin.readline().rstrip())
array = set(map(int, input().split()))

m = int(sys.stdin.readline().rstrip())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes")
    else:
        print("no")
