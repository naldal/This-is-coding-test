array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# selection
for i in range(len(array)):
    min_array = i
    for j in range(i + 1, len(array)):
        if array[min_array] > array[j]:
            min_array = j
    array[i], array[min_array] = array[min_array], array[i]

print(array)

array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# insertion
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
