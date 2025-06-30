class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if left == right:
                res.append(nums[left])
            else:
                res.append(nums[left])
                res.append(nums[right])
            left += 1
            right -= 1
        return res