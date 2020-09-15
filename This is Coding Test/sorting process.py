# 선택 정렬
# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[min_index] > arr[j]:
#             min_index = j
#     arr[min_index], arr[i] = arr[i], arr[min_index]
#
# print(arr)

# 삽입 정렬

# insert_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# for i in range(1, len(insert_arr)):
#     for j in range(i, 0, -1):
#         if insert_arr[j] < insert_arr[j-1]:
#             insert_arr[j-1], insert_arr[j] = insert_arr[j], insert_arr[j-1]
#         else:
#             break
#
# print(insert_arr)

# 퀵 정렬

# quick_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#
# quick_arr += [10]
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
#
#     return quick_sort(left_side)+[pivot]+quick_sort(right_side)
#
# print(quick_sort(quick_arr))

#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start+1
#     right = end
#
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot]
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
#
# quick_sort(quick_arr, 0, len(quick_arr) - 1)
# print(quick_arr)

# 계수 정렬

array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 100]

count = [0] * len(array)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')