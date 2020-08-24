"""Given an array of integers nums and a positive integer k, find whether
 it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
"""


def isPossibleDivide(nums, k):

    if len(nums) == k:
        return False

    toDivide = len(nums)

    if toDivide % k != 0:
        return False

    return True


test = [1, 2, 3]
k = 3
result = isPossibleDivide(test, k)
print(result)
