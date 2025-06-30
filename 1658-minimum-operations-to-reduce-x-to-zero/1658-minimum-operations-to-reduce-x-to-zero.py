class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        res = float("inf")
        prefixToIndex = dict()
        prefix = 0
        prefixToIndex[0] = -1
        for i in range(len(nums)):
            prefix += nums[i]
            if not prefix in prefixToIndex:
                prefixToIndex[prefix] = i
                if prefix == x:
                    res = min(res, i + 1)

        suffix = 0
        for i in range(len(nums) - 1, -1, -1):
            suffix += nums[i]
            needed = x - suffix
            if needed in prefixToIndex:
                prefixIndex = prefixToIndex[needed]
                if prefixIndex < i:
                    prefixLength = prefixIndex + 1
                    suffixLength = len(nums) - i
                    res = min(res, prefixLength + suffixLength)
                else:
                    return -1

        return -1 if res == float("inf") else res
        
