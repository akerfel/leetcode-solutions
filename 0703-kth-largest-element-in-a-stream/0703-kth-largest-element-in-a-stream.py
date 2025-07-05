import heapq
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class KthLargest:

    # create min heap of size k
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap) # O(n) time
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    # heappush to heap. If more than k elements: pop top
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        