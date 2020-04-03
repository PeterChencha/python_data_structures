import time
def mergesortedarrays(arr1, arr2):
    #OPERATION HAS O(nlogn)
    t = time.process_time()
    joined = arr1 + arr2
    joined.sort()
    elapsed_time = time.process_time() - t
    print (elapsed_time)
    return joined


# test_arr1 = [0,3,4,31]
# test_arr2 = [4,6,30]
#
# results = mergesortedarrays(test_arr1, test_arr2)
# print (results)

def mergesortedarraysFaster(arr1,arr2):
    #FUNCTION IS O(N) - Though in my time analysis is seems to take longer
    t = time.process_time()
    joined_array = [None] * (len(arr1)+len(arr2))
    i = 0
    j = 0
    k = 0

    #TRANSVERSE BOTH ARRAYS
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            joined_array[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            joined_array[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < len(arr1):
        joined_array[k] = arr1[i];
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < len(arr2):
        joined_array[k] = arr2[j];
        k = k + 1
        j = j + 1
    elapsed_time = time.process_time() - t
    print (elapsed_time)
    return joined_array

test_arr1 = [0,3,4,31]
test_arr2 = [4,6,30]

results = mergesortedarraysFaster(test_arr1, test_arr2)
print (results)
