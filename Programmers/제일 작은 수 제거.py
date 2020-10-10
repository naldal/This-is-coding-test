def sol(arr):
    m = min(arr)
    arr.pop((arr.index(m)))
    return [x for x in arr] or [-1]

print(sol([4,3,2,1]))