a = int(input())
b = input()

for i in range(len(b)-1, -1, -1):
    print(int(b[i])*a)
print(a*int(b))