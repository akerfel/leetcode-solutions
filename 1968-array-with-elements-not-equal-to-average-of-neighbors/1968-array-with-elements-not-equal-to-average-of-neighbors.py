class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        nums.sort()
        L = 0
        R = n - 1

        res = [-1] * n
        i = 0
        while res[-1] == -1:
            res[i] = nums[L]
            L += 1
            i += 1
            if res[-1] == -1:
                res[i] = nums[R]
                R -= 1
                i += 1
        return res