class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        L = R = len(nums) - 1
        res = 1
        remain = k
        while R >= 0 and L >= 0:
            lose = nums[R] - nums[L]
            if remain - lose < 0:
                remain += (nums[R] - nums[R - 1]) * (R - 1 - L)
                R -= 1
            else:
                remain -= lose
                res = max(res, R - L + 1)
                L -= 1
        return res
