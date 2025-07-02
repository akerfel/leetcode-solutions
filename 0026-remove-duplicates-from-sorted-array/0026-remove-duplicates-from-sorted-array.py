class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R = 0
        while (R < len(nums)):
            nums[L] = nums[R]
            while (R < len(nums) and nums[R] == nums[L]):
                R += 1
            L += 1
        return L