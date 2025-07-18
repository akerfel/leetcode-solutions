import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fromHeap = list()
        for p, f, t in trips:
            fromHeap.append((f, t, p)) # (from, to, passengers)
        heapq.heapify(fromHeap)

        toHeap = list()
        for p, f, t in trips:
            toHeap.append((t, f, p)) # (to, from, passengers)
        heapq.heapify(toHeap)

        passengers = 0
        while fromHeap:
            if passengers > capacity:
                return False
            currentStop = min(fromHeap[0][0], toHeap[0][0])

            while toHeap and toHeap[0][0] == currentStop:
                passengers -= heapq.heappop(toHeap)[2]
            while fromHeap and fromHeap[0][0] == currentStop:
                passengers += heapq.heappop(fromHeap)[2]
        
        return passengers <= capacity