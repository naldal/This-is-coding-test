def solution(arr, divisor):
    return sorted([x for x in arr if x % divisor == 0]) or [-1]


print(solution([3,2,6], 10))
