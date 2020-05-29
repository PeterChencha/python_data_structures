"""SORT THIS OUT"""
# TODO:
import time
def mergesortedarrays(arr1, arr2):
    #OPERATION HAS O(nlogn) TIME COMPLEXITY
    t = time.process_time()
    joined = arr1 + arr2
    joined.sort()
    elapsed_time = time.process_time() - t
    print("Time elapsed is {}".format(elapsed_time))
    return joined

def mergesortedarraysFaster(arr1,arr2):
    #FUNCTION IS O(N) - Though in my time analysis is seems to take longer
    t = time.process_time()

    #CHECK INPUT
    if (len(arr1) == 0):
        return arr2
    if (len(arr2) == 0):
        return arr1

    joined_array = [] * (len(arr1)+len(arr2))
    i = 0 #POINTER OF FIRST ARRAY
    j = 0 #POINTER OF SECOND ARRAY

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            joined_array.append(arr1[i])
            i = i + 1
        else:
            joined_array.append(arr2[j])
            j = j + 1

    while i < len(arr1):
        joined_array.append(arr1[i])
        i = i + 1

    while j < len(arr2):
        joined_array.append(arr2[j])
        j = j + 1
    elapsed_time = time.process_time() - t
    print("Time elapsed is {}".format(elapsed_time))
    return joined_array
test_arr1 = [0,3,4,31]
test_arr2 = [3,4,6,30,55,77]
print("Using Merge Sort")
results = mergesortedarraysFaster(test_arr1, test_arr2)
print (results)
print("Using in built sort")
results = mergesortedarrays(test_arr1, test_arr2)
print (results)
