import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dictCounter = Counter(tasks)
        heap = list() # count, label, lastUsed
        for (label, count) in dictCounter.items():
            heapq.heappush(heap, (-1 * count, label, float("-inf"))) 
        heapq.heapify(heap)

        interval = 0
        while True:
            toAdd = list()
            while heap:
                popped = heapq.heappop(heap)
                lastUsed = popped[2]
                if interval - lastUsed > n:
                    idle = False 
                    count = -1 * popped[0]
                    if count > 1:
                        updated = (-(count - 1), popped[1], interval)
                        toAdd.append(updated)
                    break
                else:
                    toAdd.append(popped)
            if not toAdd and not heap:
                break
            for t in toAdd:
                heapq.heappush(heap, t)
            interval += 1

        return interval + 1