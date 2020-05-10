from heapq import heappop, heappush, heapify
"""PYTHON BUILDS MIN HEAPS BY DEFAULT"""
heap = []
nums = [12, 3, -5, 14, 20, -100, 55]

# for num in nums:
#     heappush(heap, num)
#
# while heap:
#     print(heappop(heap))


heapify(nums)
print(nums)
