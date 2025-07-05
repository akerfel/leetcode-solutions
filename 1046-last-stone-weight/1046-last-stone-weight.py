import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(s * -1)
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -1 * heapq.heappop(heap)
            second = -1 * heapq.heappop(heap)
            if second < first:
                first -= second
                heapq.heappush(heap, -1 * first)

        if len(heap) == 1:
            return -1 * heapq.heappop(heap)
        return 0