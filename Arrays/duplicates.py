"""REMOVE DUPLICATES FROM A LIST IN ASCENDING ORDER IN PLACE"""

def removeDuplicates(data):
    length = len(data)
    index_of_last = length - 1
    current_pointer = 0
    while current_pointer < index_of_last:
        j = current_pointer + 1
        while data[current_pointer] == data[j]:
            swap(data, j, index_of_last)
            index_of_last = index_of_last - 1
            j = j + 1
            print("Result so far", data[:index_of_last+1])
        current_pointer = current_pointer + 1

    return data[:index_of_last+1]


def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

def removeDuplicatesGeeks(arr, n):
    if n == 0 or n == 1:
        return n

    # To store index of next
    # unique element
    j = 0

    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n-1]
    j += 1
    return arr[:j]
data = [1,1,2,2,2,3,4,4,5,5]
# result = removeDuplicates(data)
result_geeks = removeDuplicatesGeeks(data, len(data))
print(result_geeks)
