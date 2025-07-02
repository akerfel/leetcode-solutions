class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = 0
        R = len(height) - 1
        maxWater = 0
        while (L < R):
            water = min(height[L], height[R]) * (R - L)
            maxWater = max(water, maxWater)
            if (height[L] >= height[R]):
                R -= 1
            else:
                L += 1
        return maxWater