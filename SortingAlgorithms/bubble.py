"""O(N^2) TIME COMPLEXITY"""
def bubble(arr):

    if len(arr) == 0:
        message = "Array is empty"
        return message

    if len(arr) == 1:
        return arr

    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                tempdata = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tempdata

    return arr

array = [1,25,3,55,0]
print(bubble(array))
