# TC = nlog(n-k)
# SC = O(n-k)
# Using max heap
from heapq import heapify, heappop, heappush
import math


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        n = len(nums)
        result = math.inf
        heapify(max_heap)
        for num in nums:
            heappush(max_heap, -1 * num)
            if len(max_heap) > n - k:

                result = min(result, -1 * heappop(max_heap))

        return result


# --------------------------------------------------------------------------------------------
# TC = nlogk
# SC = O(k)
# Using min heap
from heapq import heapify, heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        heapify(result)
        for num in nums:
            heappush(result, num)
            if len(result) > k:
                heappop(result)

        return result[0]
