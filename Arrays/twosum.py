#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(arr, target):
    complement_set = set()
    indices = []
    for _ in range(len(arr)):
        if arr[_] in complement_set:
            indices.append(_)
        complement_set.add(target - arr[_])
    first_number = target - arr[indices[0]]
    first_index = arr.index(first_number)
    indices.append(first_index)
    indices.sort()
    return indices
print("Initial solution")
test_array = [1,4,3,2,6]
target = 9
result = twoSum(test_array, target)
print(result)


def twoSumOther(arr, target):
    complement_set = set()
    results = []

    for i in range(len(arr)):
        if arr[i] in complement_set:
            results.append(arr[i])
        else:
            complement_set.add(target - arr[i])

    first_number = target - results[0]
    results.append(first_number)

    return results

print("Attempt at implementation from scratch")
test_array = [1,4,3,2,6]
target = 9
result = twoSumOther(test_array, target)
print(result)
