n = 5
b = 0
l = n-2

for i in range(n, 1, -1):
    if i == n:
        print(' '*(i-1)+'*'*i)
    else:
        print(' '*(i-1)+'*'+' '*l+'*'+' '*b+'*')
        b += 1

print('*'*n+' '*l+'*')

for i in range(n):
    if i != n-1:
        print('*'+' '*l+'*'+' '*(b-1)+'*')
        b -= 1
    else:
        print('*'*n)


