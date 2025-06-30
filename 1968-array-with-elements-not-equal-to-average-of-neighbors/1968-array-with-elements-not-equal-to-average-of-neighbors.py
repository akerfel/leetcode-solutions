class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        L = 0
        n = len(nums)
        R = n - 1

        res = list()
        while (len(res) < n):
            res.append(nums[L])
            L += 1
            if (len(res) != n):
                res.append(nums[R])
                R -= 1
        return res