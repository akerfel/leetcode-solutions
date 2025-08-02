class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        zeros = 0
        res = list()
        for i in range (len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                res.append(nums[i])
        
        res += [0] * zeros

        return res