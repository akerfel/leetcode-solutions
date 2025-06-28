class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    # reverse the numbers from index L to R (inclusive) in the list
    def reverse(self, nums, L, R):
        while L < R:
            tmp = nums[L]
            nums[L] = nums[R]
            nums[R] = tmp
            L += 1
            R -= 1
