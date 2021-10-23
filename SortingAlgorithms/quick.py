def quick_sort(arr, low_index, high_index):

    if low_index >= high_index:
        return

    pivot_index = partition(arr, low_index, high_index)
    quick_sort(arr, low_index, pivot_index-1)
    quick_sort(arr, pivot_index+1, high_index)
    return arr


def partition(arr, low_index, high_index):

    pivot_index = (low_index + high_index)//2
    swap(arr, pivot_index, high_index)

    i = low_index

    for j in range(low_index, high_index):
        if arr[j] <= arr[high_index]:
            swap(arr, i, j)
            i = i + 1
    swap(arr, i, high_index)

    return i


def swap(arr, i, j):
    tempdata = arr[i]
    arr[i] = arr[j]
    arr[j] = tempdata


array = [1, 25, 3, 55, 0]
low_index = 0
high_index = len(array) - 1
print(quick_sort(array, low_index, high_index))
