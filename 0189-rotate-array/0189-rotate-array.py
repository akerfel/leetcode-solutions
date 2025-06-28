class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copy = list(nums)
        for i in range(len(nums)):
            nums[i] = copy[(i - k) % len(nums)]