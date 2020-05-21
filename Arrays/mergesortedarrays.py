"""SORT THIS OUT"""
# TODO: 
import time
def mergesortedarrays(arr1, arr2):
    #OPERATION HAS O(nlogn) TIME COMPLEXITY
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
    #STILL IN THE WORKS NEED A WAY OF MAINTAINING THAT WHILE LOOP.
    t = time.process_time()

    #CHECK INPUT
    if (len(arr1) == 0):
        return arr2
    if (len(arr2) == 0):
        return arr1

    joined_array = [] * (len(arr1)+len(arr2))
    i = 0
    j = 0
    count = 0
    #largest_length = max(len(arr1), len(arr2))
    largest_length = 6

    while (count<largest_length):
        print (arr1[i], arr2[j])
        if (arr1[i] < arr2[j]):
            joined_array.append(arr1[i])
            i = i + 1
        else:
            joined_array.append(arr2[j])
            j = j + 1
        count = count + 1
    elapsed_time = time.process_time() - t
    print (elapsed_time)
    return joined_array

test_arr1 = [0,3,4,31]
test_arr2 = [3,4,6,30]

results = mergesortedarraysFaster(test_arr1, test_arr2)
print (results)
