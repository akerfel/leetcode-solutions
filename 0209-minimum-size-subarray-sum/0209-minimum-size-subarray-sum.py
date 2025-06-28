class Solution(object):
    def minSubArrayLen(self, target, nums):
        shortest = float("inf")
        L = 0
        total = 0
        for R in range (len(nums)):
            total += nums[R]
            while (total >= target):
                shortest = min(shortest, R - L + 1)
                total -= nums[L]
                L += 1
        return 0 if shortest == float("inf") else shortest