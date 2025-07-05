import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        startHeap = list() # (enqueTime, processTime, index)
        for i, task in enumerate(tasks):
            heapq.heappush(startHeap, (task[0], task[1], i))

        time = 1
        processHeap = list() # (processTime, index), i.e. sorted first by processTime and then by index
        res = list()
        while startHeap or processHeap:
            processTime, index = self.getShortestAvailable(startHeap, processHeap, time)

            if processTime:
                time += processTime
                res.append(index)
            else:
                # If none available, jump to when earliest available
                time = startHeap[0][0]
        
        return res

    # Returns tuple (processTime, index) with shortest processTime available.
    # If multiple tasks have the shortest time then the one with smallest index is chosen.
    def getShortestAvailable(self, startHeap, processHeap, time):
        # startHeap[0] is always the element with smallest enqueTime
        while startHeap and startHeap[0][0] <= time:
            enqueTime, processTime, index = heapq.heappop(startHeap)
            heapq.heappush(processHeap, (processTime, index)) 
        
        if not processHeap:
            return (None, None) # no task available
        return heapq.heappop(processHeap)