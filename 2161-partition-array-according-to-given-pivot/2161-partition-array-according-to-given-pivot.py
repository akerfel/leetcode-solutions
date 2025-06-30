class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        start = list()
        middle = list() 
        end = list()

        for i in range(len(nums)):
            if nums[i] < pivot:
                start.append(nums[i])
            elif nums[i] > pivot:
                end.append(nums[i])
            else:
                middle.append(nums[i])
        
        return start + middle + end