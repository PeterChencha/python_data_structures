def shuffleArray(nums, n):
    leading_pointer = n
    lagging_pointer = 0
    new_array = []

    while leading_pointer < len(nums):
        new_array.append(nums[lagging_pointer])
        new_array.append(nums[leading_pointer])
        leading_pointer = leading_pointer + 1
        lagging_pointer = lagging_pointer + 1

    return new_array


test = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
result = shuffleArray(test, n)
print(result)
