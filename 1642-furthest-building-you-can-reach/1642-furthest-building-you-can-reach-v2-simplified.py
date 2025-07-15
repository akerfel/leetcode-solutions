import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 1. Use only bricks. Use max heap to keep track of largest climbs.
        # 2. When can't keep going: replace highest climb with ladder. Reclaim those bricks.
        # 3. Reapeat step 1-2 until ladders run out.

        climbs = list()
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                bricks -= diff
                heapq.heappush(climbs, - diff)

                if bricks < 0:
                    if ladders == 0:
                        return i
                    ladders -= 1
                    bricks += - heapq.heappop(climbs)

        return len(heights) - 1