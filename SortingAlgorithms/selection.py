def selection_sort(arr):

    for i in range(len(arr)-1):
        index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j

        if index != i:
            swap(arr, index, i)

    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

array = [1,25,3,55,0]
print(selection_sort(array))
