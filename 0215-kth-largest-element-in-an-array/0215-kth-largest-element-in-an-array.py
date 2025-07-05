import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for num in nums:
            heap.append(-1 * num)
        heapq.heapify(heap)

        res = 0
        for i in range(k):
           res = -1 * heapq.heappop(heap)
        
        return res
