class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        res = [0] * len(nums)

        p = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                res[p] = nums[i]
                p += 1
        
        for i in range(len(nums)):
            if nums[i] == pivot:
                res[p] = nums[i]
                p += 1
        
        for i in range(len(nums)):
            if nums[i] > pivot:
                res[p] = nums[i]
                p += 1
        
        for i in range(len(nums)):
            nums[i] = res[i]
        
        return nums