import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = list(counter.values())
        heapq.heapify(heap)

        for i in range(k):
            count = heapq.heappop(heap)
            if count > 1:
                heapq.heappush(heap, count - 1)
        
        return len(heap)