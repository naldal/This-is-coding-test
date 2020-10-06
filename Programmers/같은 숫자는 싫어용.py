def solution(arr):
    for i in range(len(arr)):
        p = arr[i]
        for j in range(i+1, len(arr)):
            if p == arr[j]:
                arr[j] = -1
            else:
                break
    answer = [x for x in arr if x >= 0]
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
