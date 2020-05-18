def merge_sort(arr):

    if len(arr) == 1:
        return
    """DIVIDE!!!"""
    middle_index = len(arr)//2
    left_half = arr[:middle_index]
    right_half = arr[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)
    """CONQUER!!!"""
    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half [j]:
            arr[k] = left_half[i]
            i = i + 1
        else:
            arr[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i < len(left_half):
        arr[k] = left_half[i]
        k = k + 1
        i = i + 1

    while j < len(right_half):
        arr[k] = right_half[j]
        k = k + 1
        j = j + 1

    return arr

array = [1,25,3,55,0,-55,22,4.5]
print(merge_sort(array))
