import time
def mergesortedarrays(arr1, arr2):
    #OPERATION HAS O(nlogn) TIME COMPLEXITY
    t = time.process_time()
    joined = arr1 + arr2
    joined.sort()
    elapsed_time = time.process_time() - t
    print (elapsed_time)
    return joined


test_arr1 = [0,3,4,31]
test_arr2 = [4,6,30]

results = mergesortedarrays(test_arr1, test_arr2)
print (results)

def mergesortedarraysFaster(arr1,arr2):
    #FUNCTION IS O(N) - Though in my time analysis is seems to take longer
    #EDITED = NOW NOT RUNNING
    t = time.process_time()
    joined_array = [None] * (len(arr1)+len(arr2))
    #CHECK INPUT
    if (len(arr1) == 0):
        return arr2
    if (len(arr2) == 0):
        return arr1

    item_arr1 = arr1[0]
    item_arr2 = arr2[0]
    i = 1
    j = 1

    #TRANSVERSE BOTH ARRAYS
    while (item_arr1 or item_arr2):
        if (item_arr2 is None or item_arr1 < item_arr2):
            joined_array.append(item_arr1)
            item_arr1 = arr1[i]
            i += 1
        else:
            joined_array.append(item_arr2)
            item_arr2 = arr2[j]
            j += 1
    elapsed_time = time.process_time() - t
    print (elapsed_time)
    return joined_array

# test_arr1 = [0,3,4,31]
# test_arr2 = [3,4,6,30]
#
# results = mergesortedarraysFaster(test_arr1, test_arr2)
# print (results)
