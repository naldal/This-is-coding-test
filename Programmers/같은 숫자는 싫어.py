def solution(arr):
    p = 0
    for i in range(len(arr)):
        p = arr[i]
        for j in range(1, len(arr)):
            if p == arr[j]:
                arr.pop(j)
            else:
                break
    return arr

print(solution([1,1,3,3,0,1,1]))