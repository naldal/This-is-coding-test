import bisect, random


# 이진 탐색 (특정요소존재 검사)
def binary_search(arr, x):
    i = bisect.bisect_left(arr, x)
    print(i)
    return i < len(arr) and arr[i] == x


print(binary_search([1, 2, 3, 4, 5], 5))


# 리스트 정렬하기
a = []
b = [random.randrange(1, 50) for _ in range(50)]
for x in b:
    bisect.insort(a, x)
print(a)


# 점수에 따라 등급나누기
def get_grade(score):
    r = (50, 60, 70, 90, 100)
    g = 'FDCBA'
    return g[bisect.bisect_right(r, score)]


print(get_grade(70))
