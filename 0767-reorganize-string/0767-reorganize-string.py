import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = list() # (-count, char)
        for char, count in counter.items():
            heap.append((-count, char))
        heapq.heapify(heap)
        
        res = list()
        while heap:
            count, char = heapq.heappop(heap)
            # If max count char is same as last used then use second highest count.
            if res and char == res[-1]:
                if not heap:
                    return ""
                usedLast = (count, char)
                count, char = heapq.heappop(heap)
                heapq.heappush(heap, usedLast)
            count *= -1
            if count > 1:
                count -= 1
                heapq.heappush(heap, (-count, char))
            else:
                usedLast = None
            res.append(char)

        return "".join(res)