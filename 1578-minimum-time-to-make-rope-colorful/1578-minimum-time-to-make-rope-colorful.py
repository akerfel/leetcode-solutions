class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # for each subarray where all elements are equal:
        # res += sum(subarray) - max(subarray)
        # use L and R pointer, increment R while property holds,
        # keep track of both sum and max.

        res = 0
        L = 0
        while L < len(colors) - 1:
            R = L + 1
            total = neededTime[L]
            maximum = neededTime[L]
            while R < len(colors) and colors[L] == colors[R]:
                maximum = max(maximum, neededTime[R])
                total += neededTime[R]
                R += 1
            res += total - maximum

            L = R
        
        return res