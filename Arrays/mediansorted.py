""" Median of Two Sorted Arrays"""

def findMedianSortedArrays(nums1, nums2):
    i = 0
    j = 0
    sorted_array = [] * (len(nums1)+len(nums2))

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sorted_array.append(nums1[i])
            i = i + 1
        else:
            sorted_array.append(nums2[j])
            j = j + 1

    while i < len(nums1):
        sorted_array.append(nums1[i])
        i = i + 1

    while j < len(nums2):
        sorted_array.append(nums2[j])
        j = j + 1

    if len(sorted_array) % 2 == 0:
        right_pointer = len(sorted_array)/2
        left_pointer = right_pointer - 1
        median = float((sorted_array[left_pointer] + sorted_array[right_pointer]))/2
        return median
    else:
        pointer = len(sorted_array)/2
        median = sorted_array[pointer]
        return median

test1 = [1,3]
test2 = [2]
result = findMedianSortedArrays(test1, test2)
print(result)
