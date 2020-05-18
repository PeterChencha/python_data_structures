def insertion_sort(arr):

    for i in range(len(arr)):
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j, j-1)
            j = j-1

    return arr

def swap(arr, i, j):
    tempdata = arr[i]
    arr[i] = arr[j]
    arr[j] = tempdata

array = [1,25,3,55,0]
print(insertion_sort(array))
