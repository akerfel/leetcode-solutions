class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return true if koko can finish with k = speed
        def canFinish(speed):
            time = 0
            for p in piles:
                time += p // speed
                if p % speed > 0:
                    time += 1
            return time <= h

        # binary search for k
        L = 1
        R = max(piles) # k should never be larger than the biggest pile
        res = -1
        while L <= R:
            m = L + ((R - L) // 2)
            
            if canFinish(m):
                R = m - 1
                res = m
            else:
                L = m + 1

        return res