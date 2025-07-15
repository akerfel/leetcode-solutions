import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 1. Use only bricks. Use max heap to keep track of largest climbs.
        # 2. When can't keep going: replace highest climb with ladder. Reclaim those bricks.
        # 3. Reapeat step 1-2 until ladders run out.

        climbs = list()
        i = 0
        while i < len(heights) - 1:
            h1 = heights[i]
            h2 = heights[i + 1]
            diff = h2 - h1
            if diff > 0:
                if bricks >= diff:
                    bricks -= diff
                    heapq.heappush(climbs, - diff)
                else:
                    if ladders > 0:
                        ladders -= 1
                        if len(climbs) > 0:
                            heapq.heappush(climbs, - diff)
                            bricks -= diff
                            highestClimb = - heapq.heappop(climbs)
                            bricks += highestClimb
                    else:
                        break
            i += 1

        return i