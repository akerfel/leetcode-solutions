class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
         # find widest window which sums exactly to target
        target = sum(nums) - x

        res = float("inf")
        L = 0
        cur = 0
        for R in range(len(nums)):
            cur += nums[R]
            while cur > target and L <= R:
                cur -= nums[L]
                L += 1
            if cur == target:
                width = R - L + 1
                res = min(res, len(nums) - width)
        
        return -1 if res == float("inf") else res
